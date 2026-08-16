from db import engine
from tables import users, posts
from sqlalchemy import text

#using Raw sql (Insert)
def raw_sql_insert():
    with engine.connect() as conn:
        stmt = text("""
                    INSERT INTO users(name, email)
                    values (:name, :email)
                    """)
        conn.execute(stmt,{"name": "abhay","email":"Abhay@gmail.com."})
        conn.commit()

# Using RAW SQL (SELECT)
def raw_sql_example():
    with engine.connect() as conn:
        stmt = text("""
                    SELECT * FROM users 
                    where email = :email
                    """)
        result = conn.execute(stmt,{"email": "abhay@gmail.com"}).first()
        return result