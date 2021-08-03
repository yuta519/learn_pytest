from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker


def get_postgres_url() -> str:
    username = "postgres"
    password = "pass"
    hostname = "localhost"
    port = "5432"
    dbname = "postgres"
    return (f"postgresql+psycopg2://{username}:{password}"
            f"@{hostname}:{port}/{dbname}")


engine = create_engine(
    url=get_postgres_url(),
    echo=False,
    executemany_mode="values_plus_batch",
    executemany_values_page_size=10000,
    executemany_batch_page_size=500,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Generator[Session, None, None]:
    session: Session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


Base = declarative_base()
