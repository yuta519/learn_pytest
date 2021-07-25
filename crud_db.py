import psycopg2
from sqlalchemy import create_engine

def get_connection():
    # dsn = (f"postgresql+psycopg2://postgres:@127.0.0.1:5433/postgres")
    dsn = ("dbname=postgres  user=postgres password= host=localhost port=5433")
    return psycopg2.connect(dsn) 


if __name__ == '__main__':
    conn = get_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    cur.close()
    conn.close()