from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from typing import Annotated
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

# POST: handle form submission
@app.post("/login/")
async def login(username:Annotated[str,Form(min_length=3)],
                password:Annotated[str,Form(min_length=3,max_length=20)]):
    print(username,password)
    return {"username":username,"password":len(password)}