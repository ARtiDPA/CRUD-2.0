from sqlalchemy import create_engine
import sqlalchemy


engine = create_engine("postgresql+psycopg2://postgres:password@localhost:5432/postgres")

connection = engine.connect()


metadate = sqlalchemy.MetaData()


users = sqlalchemy.Table("user", metadate,
                        sqlalchemy.Column("id", sqlalchemy.Integer),
                        sqlalchemy.Column("name", sqlalchemy.Text),
                        sqlalchemy.Column("first_name", sqlalchemy.Text),
                        sqlalchemy.Column("date", sqlalchemy.Text),
                        sqlalchemy.Column("Sity", sqlalchemy.Text),
                        sqlalchemy.Column("gender", sqlalchemy.Text),
                        sqlalchemy.Column("number", sqlalchemy.Text),
                        sqlalchemy.Column("mail", sqlalchemy.Text)
                        )