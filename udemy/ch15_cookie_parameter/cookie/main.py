from fastapi import FastAPI,Cookie
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()
@app.get("/products/recommendations")
async def get_recommendations(session_id:Annotated[str |None,Cookie()]=None):
    print(session_id)
    if session_id:
        return {"message":f'recommendations for session {session_id}',"session_is":session_id}
    return {"message":"No session ID provided, showing default recommendations"}

#cmd
# C:\Users\abhay>curl -H "Cookie:session_id=abc123" http://127.0.0.1:8000/products/recommendations
