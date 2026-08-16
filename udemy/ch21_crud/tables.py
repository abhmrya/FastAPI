from db import engine
from sqlalchemy import MetaData, Table, Integer, String, Column,ForeignKey

metadata = MetaData()

# User Table
users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50), nullable=False),
    Column("email", String, nullable=False, unique=True),
)

posts = Table(
    "posts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id",Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False),
    Column("title", String, nullable=False),
    Column("content",String,nullable=False)
)

# create table in database
def create_tables():
    metadata.create_all(engine)
