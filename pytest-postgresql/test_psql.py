# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
# from sqlalchemy.orm import sessionmaker

from models import User


def test_insert_user_data(setup_database: Session) -> None:
    try:
        user = User(
            user_name="Yuta",
            user_age=28
        )
        setup_database.add(user)
        setup_database.commit()
    except RuntimeError:
        print(RuntimeError)
        setup_database.rollback()

    users = setup_database.query(User).filter(User.user_name=="Yuta").all()
    for user in users:
        assert user.user_name == "Yuta"
    