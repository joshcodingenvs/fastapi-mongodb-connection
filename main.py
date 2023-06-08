# import modules/packages
from fastapi import FastAPI
from database.connection import init

# import routes
from routes.routes import router

# app instance
app = FastAPI()

# connect to database on app startup event
@app.on_event("startup")
async def on_startup():
    await init()


# configure routes
app.include_router(router)