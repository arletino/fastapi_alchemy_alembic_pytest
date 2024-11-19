'''
Тест может обнаружить забытые методы downgrade, 
не удаленные типы данных в методах downgrade,
и другие ошибки.

Не требует изменения - можем просто добавить в проект и 
обнаруживать до 80% типовых ошибок в миграциях
'''
import pytest

from alembic.command import downgrade, upgrade 
from alembic.config import Config 
from alembic.script import Script, ScriptDirectory 
from tests.db_utils import alembic_config_from_url 

def get_revisions():
    # Создаем объект конфигурации Alembic
    # (нам не нужна база данны для получения списка версий)
    config = alembic_config_from_url()

    # Получим объект директорию миграций Alembic
    revisions_dir = ScriptDirectory.from_config(config) 

    # Отсортируем список миграций от первой к последней
    revisions = list(revisions_dir.walk_revisions('base', 'heads')) 
    revisions.reverse()
    return revisions 

@pytest.mark.parametrize('revision', get_revisions())
def test_migrations_stairway(alembic_config: Config, revision: Script):
    upgrade(alembic_config, revision.revision)

    #  '-1' - для отката на первую миграцию
    downgrade(alembic_config, revision.down_revision or '-1')
    upgrade(alembic_config, revision.revision)