from fastapi import FastAPI

app = FastAPI(title="Knowledge Explorer")


@app.get("/")
def root():
    return {
        "message": "Knowledge Explorer is alive!"
    }