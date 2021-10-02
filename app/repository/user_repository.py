from database.model.master import MasterUser
from database import session
from sqlalchemy import or_


def add(id):
    user = MasterUser(
        id=id
    )
    try:
        session.add(user)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()


def add_all(ids: list):
    users = [MasterUser(id=id) for id in ids]
    try:
        session.add_all(users)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()


def find_all(ids: list) -> list:
    filter = [MasterUser.id == id for id in ids]
    try:
        users = session.query(
            MasterUser.id
        ).filter(or_(*filter)).all()
        return users
    except Exception as e:
        print(e)
