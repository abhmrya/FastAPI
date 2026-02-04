from fastapi import FastAPI, Form,Depends
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel,Field
app = FastAPI()

# GET: show login form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login</title>
    </head>
    <body>
        <h2>Login Form</h2>
        <form method="post" action="/login/">
            <label>Username:</label><br>
            <input type="text" name="username" required><br><br>

            <label>Password:</label><br>
            <input type="password" name="password" required><br><br>

            <input type="submit" value="Login">
        </form>
    </body>
    </html>
    """

#pydantic model from From
class FormData(BaseModel):
    username:str=Field(min_length=3)
    password:str = Field(min_length=3,max_length=20)
    model_config={"extra":"forbid"}

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        password: str = Form(...)
    ):
        return cls(username=username, password=password)

@app.post("/login/")
async def login(data: FormData = Depends(FormData.as_form)):
    return data