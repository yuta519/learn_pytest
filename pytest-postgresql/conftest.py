import tempfile

import pytest
from pytest_postgresql import factories
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models import Base, User


socket_dir = tempfile.TemporaryDirectory()
postgresql_my_proc = factories.postgresql_proc(
    port=None, 
    unixsocketdir=socket_dir.name
)
postgresql_my = factories.postgresql('postgresql_my_proc')


@pytest.fixture(scope='function')
def setup_database(postgresql_my):

    def dbcreator():
        return postgresql_my.cursor().connection

    engine = create_engine('postgresql+psycopg2://', creator=dbcreator)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# end setup_database()


# def test_connection(transacted_postgresql_db):
#     instance = Person(name='Foo Bar')
#     transacted_postgresql_db.session.add(instance)
#     transacted_postgresql_db.session.commit()

#     transacted_postgresql_db.connection.execute('DROP TABLE my_table')

@pytest.fixture
def database_session(postgresql_my):

    def dbcreator():
        return postgresql_my.cursor().connection

    engine = create_engine('postgresql+psycopg2://', creator=dbcreator)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

@pytest.fixture
def testdata_for_root(database_session):
    session = database_session

    try:
        user = User(
            user_name="Yuta",
            user_age=28
        )
        session.add(user)
        session.commit()
        yield session
    except RuntimeError:
        print(RuntimeError)
        session.rollback()
    finally:
        
        session.close()
