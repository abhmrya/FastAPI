from fastapi import FastAPI, File,UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
import uuid
import shutil


app = FastAPI()

# GET: show upload form
@app.get("/", response_class=HTMLResponse)
async def get_form():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Upload</title>
    </head>
    <body>
        <h2>Single File Upload (bytes)</h2>
        <form enctype="multipart/form-data" method="post" action="/files/">
            <input name="file" type="file">
            <input type="submit" value="Upload">
        </form>

        <h2>Single File Upload (UploadFile)</h2>
        <form enctype="multipart/form-data" method="post" action="/uploadfiles/">
            <input name="file" type="file">
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    """

# POST: receive file
# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     if not file:
#         return {"message":"No file sent"}
#     return {
#         "filename": "uploaded_file",
#         "size_in_bytes": len(file)
#     }

# @app.post("/files/")
# async def create_file(file: Annotated[bytes, File()]):
#     if not file:
#         return {"message":"No file sent"}
#     filename=f"{uuid.uuid4()}.bin"
#     save_path = f"uploads/{filename}"
#     os.makedirs("uploads",exist_ok=True)
#     with open(save_path,"wb") as buffer:
#         buffer.write(file)
#     return {
#         "filename": "uploaded_file",
#         "size_in_bytes": len(file)
#     }

@app.post("/uploadfiles")
async def create_upload_file(file:Annotated[UploadFile | None,File()]=None):
    if not file:
         return {"message":"No upload file sent"}
    save_path = f"uploads/{file.filename}"
    os.makedirs("uploads",exist_ok=True)
    with open(save_path,"wb") as buffer:
        shutil.copyfileobj(file.file,buffer)
    return {"filename":file.filename,"content_type":file.content_type}
    