Fastapi, async SQLAlchemy, pytest, and Alembic (all using asyncpg)  

Task manager for asyncio is taskiq

Устанавливаем зависимости для релиза проекта  

```$ poetry add fastapi uvicorn uvloop asyncpg alembic pydantic-settings```  
```$ poetry add sqlalchemy --extras asynci```

Устанавливаем зависимости для разработки и тестирования в **--dev**

```$ poetry add --group=dev httpx sqlalchemy-utils pytest yarl mypy black isort```  

Я использую файл __init__ в модуле orm, чтобы иметь возможность использовать import orm, а затем вызывать такие объекты, как orm.db_manager, orm.User и т.д. Такой подход существенно упрощает различие между вашими моделями SQLAlchemy и бизнес-ориентированными моделями.  

Creating the API views

Модель UserResponse имеет все поля, которые уже совместимы с json (строки и дюймы). Вот почему мы можем использовать .model_dump(). 
Если ваша модель имеет некоторые типы, такие как UUID, datetime, другие классы, - вы можете использовать .model_dump (mode='json'), и pydantic автоматически преобразует выходные значения в типы, поддерживаемые json.

Предпочитаю возвращать Response напрямую, чем использовать преобразование ответной_модели FastAPI. 
Для меня это удобнее плюс на самом деле быстрее. 
(Вы можете проверить https://github.com/falkben/fastapi_experiments/ -> orjson_response.py)

Для простоты я выполняю запросы ORM прямо в представлениях api. В более крупном проекте лучше создать дополнительный уровень обслуживания и поместить все запросы orm/sql в один модуль. Если такие запросы распространятся по вашей кодовой базе, вы пожалеете об этом позже.

Migrations with Alembic
Чтобы начать с алембика, мы можем использовать команду alembic init для создания конфигурации алембика. Для этого мы будем использовать шаблон async:

```alembic init -t async alembic```  

alembic.ini  

Отменим комментарий к строке file_template, чтобы имена миграций были более удобными для пользователя и имели даты, чтобы мы могли их отсортировать.

alembic/env.py  

Во-первых, нам нужно будет импортировать наши модели баз данных, 
чтобы они были добавлены в объект Base.metadata. 
Это происходит автоматически, когда модель наследуется от OrmBase, 
но нам нужно импортировать модели, чтобы гарантировать, 
что они импортированы до загрузки конфигурации с алембикой. 
Поскольку мы помещаем все модели в orm/__init__.py, 
мы можем импортировать orm, и модели будут загружены.
Затем нам нужно установить конфигурацию sqlalchemy.url для использования строки подключения к базе данных.

Важное примечание. Мы собираемся создать конфигурацию Alembic для тестов, поэтому нам нужно быть осторожными и не переписывать sqlalchemy.url, если он уже установлен.

И, наконец, мы укажем целевые метаданные на наш объект Base.metadata.

Ниже я покажу изменения, которые нам необходимо внести в файл alembic/env.py:

```# alembic/env.py 
    import orm
    from app.settings import settings
    current_url = config.get_main_option('sqlalchemy.url', None)
    if not current_url:
        config.set_main_option("sqlalchemy.url", settings.database_url)
    target_metadata = orm.OrmBase.metadata```
