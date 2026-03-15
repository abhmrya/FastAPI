from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from typing import Annotated
import os
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
        <h2>Multiple File Upload</h2>
        <form enctype="multipart/form-data" method="post" action="/uploadfiles">
            <input name="files" type="file" multiple>
            <input type="submit" value="Upload">
        </form>
    </body>
    </html>
    """

@app.post("/uploadfiles")
async def create_upload_file(files: Annotated[list[UploadFile], File()]):
    if not files:
        return {"message": "No files uploaded"}

    os.makedirs("uploads", exist_ok=True)
    saved_files = []

    for file in files:
        save_path = f"uploads/{file.filename}"
        with open(save_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        saved_files.append({"filename": file.filename})

    return saved_files
