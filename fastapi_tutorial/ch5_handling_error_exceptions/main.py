from fastapi import FastAPI,HTTPException,status
from starlette.responses import JSONResponse
app = FastAPI()

#custom error handler

@app.exception_handler(HTTPException)
async def http_exception_handler(request,exc):
    return JSONResponse(status_code=200,content={"message":"oops! somthing went wrong"})

@app.get("/error_endpoint")
async def raise_exception():
    raise HTTPException(status_code=400)

import json
from fastapi import Request,status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return user

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request:Request,
                                       exc:RequestValidationError):
    body = await request.body()
    return PlainTextResponse("This is a plain text response:"
                             f"{request.method} {request.url.path}\n"
                            f"{body.decode()}\n\n"
                             f"\n{json.dumps(exc.errors(),indent=3)}",
                             status_code=status.HTTP_400_BAD_REQUEST,)