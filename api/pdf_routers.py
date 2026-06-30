from fastapi import (APIRouter,UploadFile,File)

router = APIRouter(
    prefix="/pdf",
    tags=["PDF"]
)

@router.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    contents = await file.read()
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(contents)

    return {
        "filename": file.filename,
        "status": "uploaded"
    }