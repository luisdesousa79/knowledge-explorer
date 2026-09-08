from services.document_service import save_document
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

    contents = await file.read()

    await save_document(file.filename, contents)
    
    return {
        "filename": file.filename,
        "size": len(contents)
    }
