import tempfile

import pytest
from pytest_postgresql import factories
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base


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