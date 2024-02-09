from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped
import database


class user(database.Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(32), nullable=False)
    surname: Mapped[str] = mapped_column(String(32), nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)
    gender: Mapped[int] = mapped_column(String(10), nullable=False)


def create_tables():
    database.Base.metadata.create_all(database.engine)
