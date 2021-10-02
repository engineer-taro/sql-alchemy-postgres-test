from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker

from database import settings
import sys
# moduleのimportエラーが出る場合は以下にappフォルダへの絶対パスを記載
# sys.path.append("c:\\Users\\user.name\\~~~~~~\\SQL_docker_env\\app")


_DATABASE = 'postgresql+psycopg2://%(user)s:%(password)s@%(host)s:%(port)s/%(dbname)s' % {
    'user': settings.POSTGRES_USER,
    'password': settings.POSTGRES_PASSWORD,
    'host': settings.POSTGRES_HOST,
    'port': settings.POSTGRES_PORT,
    'dbname': settings.POSTGRES_DB,
}

_engine = create_engine(
    _DATABASE,
    encoding='utf-8',
    connect_args={
        'options': f'-csearch_path={settings.POSTGRES_SCHEMA}'
    },
    echo=True
)

session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=_engine
    )
)
