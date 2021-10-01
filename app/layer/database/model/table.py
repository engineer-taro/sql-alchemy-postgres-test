from sqlalchemy import Column, String, DateTime, Integer, Text

from .base import Base


class MasterUser(Base):
    __tablename__ = 'user_table'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(20))
    age = Column(Integer)
