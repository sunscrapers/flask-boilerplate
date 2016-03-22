import pytest

from app import create_app
from database import db as _db
from tests.client import ApiTestingResponse


@pytest.yield_fixture(scope='session')
def app():
    app = create_app(config_file='config/testing.py')
    app.response_class = ApiTestingResponse
    ctx = app.app_context()
    ctx.push()

    yield app

    ctx.pop()


@pytest.yield_fixture(scope='session')
def db(app):
    _db.create_all()

    yield _db

    _db.drop_all()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.yield_fixture(scope='function')
def session(db):
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection)
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()
