from sqlalchemy.orm import declarative_base
from sqlalchemy import String, Integer, create_engine, Column
import database

engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")
Base = declarative_base()


class user(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    suename = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)


def create_tables():
    Base.metadata.create_all(database.engine)
