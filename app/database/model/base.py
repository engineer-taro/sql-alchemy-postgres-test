from sqlalchemy.ext.declarative import declarative_base
from database import session


Base = declarative_base()
Base.query = session.query_property()
