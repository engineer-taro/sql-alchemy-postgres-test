import uuid
from database.model.master import MasterUser, UserScore
from database import session


def add(user_id: int, subject: str, score: int):
    score = UserScore(
        id=uuid.uuid4(),
        user_id=user_id,
        subject=subject,
        score=score
    )
    try:
        session.add(score)
        session.commit()
    except Exception as e:
        session.rollback()
        print(e)
    finally:
        session.close()


def get_join(user_id):
    user_score = session.query(
        MasterUser.id,
        UserScore.subject,
        UserScore.score
    ).join(
        MasterUser, (
            MasterUser.id == UserScore.user_id
        )
    ).filter(
        MasterUser.id == user_id
    ).all()
    return user_score
