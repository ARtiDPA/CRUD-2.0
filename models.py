from sqlalchemy.orm import declarative_base, mapped_column, Mapped
from sqlalchemy import String, Integer, create_engine


engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")
Base = declarative_base()


class user(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(32))
    surname: Mapped[str] = mapped_column(String(32))
    age: Mapped[int] = mapped_column(Integer)
    gender: Mapped[str] = mapped_column(String(10))