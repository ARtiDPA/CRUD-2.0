from sqlalchemy import String, Integer, Column
import database


class user(database.Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(32), nullable=False)
    suename = Column(String(32), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)


def create_tables():
    database.Base.metadata.create_all(database.engine)
