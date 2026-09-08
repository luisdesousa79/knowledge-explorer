from pathlib import Path

UPLOADS_DIR = Path(__file__).resolve().parent.parent / "uploads"

async def save_document(filename: str, contents: bytes) -> None:
    UPLOADS_DIR.mkdir(exist_ok=True)
    destination = UPLOADS_DIR / filename
    with open(destination, "wb") as file:
    file.write(contents)

