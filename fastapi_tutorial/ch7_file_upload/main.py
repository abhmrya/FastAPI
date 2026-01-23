import shutil
from fastapi import FastAPI,HTTPException
from typing import Optional
from database import SessionLocal
from models import User
from fastapi import FastAPI,File,UploadFile,Path
from fastapi.responses import FileResponse
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/uploadfile")
async def upload_file(
    file: UploadFile=File(...)):
    with open(f"uploads/{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {"filename":file.filename}

@app.get("/downloadfile/{filename}",response_class=FileResponse,)
async def dounload_file(filename:str):
    if not Path(f"uploads/{filename}").exist():
        raise HTTPException(status_code=404,details=f"file {filename} not found",)
    return FileResponse(path = f"uploads/{filename}",filename=filename)