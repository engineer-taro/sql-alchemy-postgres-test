from repository import user_repository, user_score_repository
from database import session
from database.model.master import UserScore, MasterUser


if __name__ == '__main__':
    # テストしたいコードを記載
    user_repository.add_all([1, 2, 3, 4, 5])
    user_repository.find_all([1, 2, 3, 4, 5])

    user_score_repository.add(1, 'Math', 98)
    user_score_repository.get_join(1)
