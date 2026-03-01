from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
def register_face():
    return {"status": "success"}
