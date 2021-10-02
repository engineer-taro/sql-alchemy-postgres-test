from sqlalchemy import Column, String, DateTime, Integer, Text

from .base import Base


class MasterUser(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20))
    age = Column(Integer)


class UserScore(Base):
    __tablename__ = 'user_score'

    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, nullable=False)
    subject = Column(String(20))
    score = Column(Integer)