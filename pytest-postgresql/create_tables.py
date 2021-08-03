from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from models import Base, User

username = "postgres"
password = "pass"
hostname = "localhost"
port = "5432"
dbname = "postgres"

flag = 0

connection = (f"postgresql+psycopg2://{username}:{password}"
              f"@{hostname}:{port}/{dbname}")

engine = create_engine(
    url=connection,
    echo=False,
    executemany_mode="values_plus_batch",
    executemany_values_page_size=10000,
    executemany_batch_page_size=500,
)
Base.metadata.create_all(engine)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def insert_dummy_data(session: Session) -> None:
    try:
        user = User(
            user_name="Yuta",
            user_age=28
        )
        session.add(user)
        session.commit()
    except RuntimeError:
        print(RuntimeError)
        session.rollback()
    finally:
        session.close()

insert_dummy_data(SessionLocal())


if flag == 1:
    Base.metadata.drop_all(engine)
else:
    pass
