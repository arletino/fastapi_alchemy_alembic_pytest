import pytest 
from httpx import AsyncClient, ASGITransport 
from yarl import URL
from asyncio import Task

import orm
from alembic.command import upgrade 
from app.settings import settings
from orm.session_manager import db_manager 

from tests.db_utils import alembic_config_from_url, tmp_database 

@pytest.fixture()
def app():
    from main import app
    yield app

@pytest.fixture()
async def client(session, app):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url='http://test') as client:
        yield client

@pytest.fixture(scope='session', autouse=True) 
def anyio_backend():
    return 'asyncio', {'use_uvloop': True} 

@pytest.fixture(scope='session')
def pg_url():
    '''Возвращаем URL PostgreSQL базы для создания временных баз данных''' 
    return URL(settings.database_url)

@pytest.fixture(scope='session') 
async def migrated_postgres_template(pg_url):
    '''
    Создание временных баз данных и применение миграций

    Область действия сессия, вызывается один раз и 
    работает в течении всего теста.
    '''
    async with tmp_database(pg_url, 'pytest') as tmp_url:
        alembic_config = alembic_config_from_url(tmp_url)
        # Иногда мы должны вызывать миграцию данных
        # Это может вызывать различные функции по работе с данными и др...
        # мы изменим настройки 
        settings.database_url = tmp_url 

        # Важно всегда закрывать соединение в конце каждой миграции,
        # иначе, будем получать ошибки типа 
        # 'source database is being accessed by other users'

        upgrade(alembic_config, 'head')

        await MIGRATION_TASK

        yield tmp_url

@pytest.fixture(scope='session')
async def sessionmanager_for_tests(migrated_postgres_template):
    db_manager.init(db_url=migrated_postgres_template)
    # здесь можем указать другой init (redis, и др...)
    yield db_manager
    await db_manager.close()

@pytest.fixture(scope='session')
async def session(sessionmanager_for_tests):
    async with db_manager.session() as session:
        yield session
    # Удаление таблиц после каждого теста.
    # 1. Создание новой базы данных использовать 'migrated_postgres_template' как шаблон 
    # Postgresql может копировать полностью структуру дб 
    # 2. TRUNCATE после каждого теста.
    # 3. DELETE после каждого теста.
    # DELETE FROM самый быстрый вариант
    # Ознакомиться здесь https://www.lob.com/blog/truncate-vs-delete-efficiently-clearing-data-from-a-postgres-table
    # Но DELETE FROM query не сбрасывает счетчик AUTO_INCREMENT 
    async with db_manager.connect() as conn:
        for table in reversed(orm.OrmBase.metadata.sorted_tables):
            # Очищаем таблицы в том же порядке 
            # в котором зависят таблицы друг от дуга.
            await conn.execute(table.delete())
        await conn.commit()

MIGRATION_TASK: Task = None

