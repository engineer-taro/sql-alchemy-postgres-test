from layer.database.model.table import MasterUser
from layer.database import session
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


if __name__ == '__main__':
    # Input test code. JP:テストしたいコードを記載
    add(1)
    add_all([4, 5, 6])
    exists_users = find_all([1, 2, 3])
    for user in exists_users:
        print(user.id)
