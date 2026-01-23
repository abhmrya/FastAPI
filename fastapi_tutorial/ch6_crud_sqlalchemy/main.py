from database import engine
from  models import UserBody,User
import models
from sqlalchemy.orm import Session
from fastapi import FastAPI

models.Base.metadata.create_all(bind=engine)
# models.Base.metadata.create_all(bind=engine)

from database import SessionLocal
from fastapi import Depends

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

# Creating a new user
@app.post("/user")
def add_new_user(user:UserBody,
                 db:Session=Depends(get_db)):
    new_user = User(name=user.name,email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# reading the users
@app.get("/users")
def read_users(db:Session=Depends(get_db)):
    users = db.query(User).all()
    return users

#Reading a specific user
from fastapi import HTTPException,status

@app.get("/user/{user_id}")
def get_user(
    user_id:int,
    db:Session=Depends(get_db),
    ):
    user = db.query(User).filter(User.id==user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@app.post("/update/{user_id}")
def update_user(
    user_id:int,
    name:str,
    email:str,
    db:Session=Depends(get_db),
):
    db_user =db.query(User).filter(User.id==user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user is not find")
    db_user.name = name
    db_user.email = email
    db.commit()
    db.refresh(db_user)
    return db_user

@app.delete("/delete/{user_id}")
def delete_user(user_id:int,
                db:Session=Depends(get_db)):
    db_user=db.query(User).filter(User.id==user_id).first()
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User is not found")
    a =db.delete(db_user)
    print(a)
    db.commit()
    return db_user