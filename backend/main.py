from pathlib import Path
from pydantic import BaseModel
from fastapi import FastAPI, UploadFile


app = FastAPI(title="Knowledge Explorer")


@app.get("/")
def root():
    return {
        "message": "Knowledge Explorer is alive!"
    }

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users")
def create_user(user: UserCreate):

    print(user)

    return {
        "message": f"Olá {user.name}!"
    }

@app.post("/documents")
async def upload_document(file: UploadFile):

    uploads_dir = Path("uploads")
    uploads_dir.mkdir(exist_ok=True)

    destination = uploads_dir / file.filename

    

    contents = await file.read()

    print(type(contents))

    print(len(contents))

    with open(destination, "wb") as f:
        f.write(contents)
    
    return {
        "filename": file.filename,
        "size": len(contents)
    }
