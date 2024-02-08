from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine


engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")
Base = declarative_base()
connect = engine.connect()
