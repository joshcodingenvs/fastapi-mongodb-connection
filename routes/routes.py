# import modules/packages
from fastapi import APIRouter
from models.todo import Todo

# router instance
router = APIRouter()

# endpoints
@router.get("/")
async def home(todo: Todo):
    return "welcome dev"
