from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_cameras():
    return [{"id": 1, "name": "Main Entrance"}]
