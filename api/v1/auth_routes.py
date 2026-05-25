from fastapi import APIRouter

router = APIRouter()

@router.post("/register")
async def register_user():
    pass

@router.get("/login")
async def login_user():
    pass
