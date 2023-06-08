from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from models.todo import Todo

async def init():
    # create client
    client = AsyncIOMotorClient(
        "mongodb://127.0.0.1:27017"
    )

    # create the database name
    db = client["fastapi-mongodb-api"]

    # initialize beanie
    await init_beanie(database=db, document_models=[Todo])