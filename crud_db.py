import psycopg2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_connection():
    # dsn = "postgresql+psycopg2://yuta519:@127.0.0.1:5433/tests"
    # dsn = "postgresql+psycopg2://yuta519:@127.0.0.1:5433/tests"
    dsn = ("dbname=tests  user=yuta519 password= host=localhost port=5433")
    # engine = create_engine(dsn)

    # Create test database and tables
    # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
 
    return psycopg2.connect(dsn) 


if __name__ == '__main__':
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM mybook')
    rows = cur.fetchall()
    cur.close()
    conn.close()
    print(rows)