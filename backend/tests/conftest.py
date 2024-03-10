import os

import pytest
import pytest_asyncio
from alembic import command
from alembic.config import Config
from sqlalchemy_utils import create_database, drop_database, database_exists

os.environ["TESTING"] = "True"
from models import database


def create_db():
    """Create new DB for tests"""
    
    if not database_exists(database.TEST_SQLALCHEMY_DATABASE_URL):
        create_database(database.TEST_SQLALCHEMY_DATABASE_URL)
    # query = 'CREATE EXTENSION IF NOT EXISTS "uuid-ossp"'
    # database.extension_query(query=query)

    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    alembic_cfg = Config(os.path.join(base_dir + '/backend', "alembic.ini"))
    command.upgrade(alembic_cfg, "head")


@pytest_asyncio.fixture
async def temp_db_async():
    create_db()
    try:
        await database.database.connect()
        yield
        await database.database.disconnect()
    finally:
        pass
        drop_database(database.TEST_SQLALCHEMY_DATABASE_URL)


@pytest.fixture
def temp_db_sync():
    create_db()
    try:
        yield database.TEST_SQLALCHEMY_DATABASE_URL
    finally:
        drop_database(database.TEST_SQLALCHEMY_DATABASE_URL)


# @pytest.fixture
# def set_data():
#     query = 'INSERT INTO "Contact" (name, description) VALUES (\'Ivan\', \'My friend\');'
#     database.extension_query(query=query)
