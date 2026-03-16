from db import engine
from sqlalchemy import MetaData, Table, Integer, String, Column

metadata = MetaData()

# User Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String, nullable=False, unique=True)
)

# create table in database
def create_tables():
    metadata.create_all(engine)

# drop table
# def drop_tables():
#     metadata.drop_all(engine)