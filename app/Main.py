from fastapi import FastAPI
from app.repositories.DataBase import DBase,Engine
from app.controllers.routes import router
import uvicorn

DBase.metadata.create_all(bind=Engine)
app = FastAPI()
app.include_router(router=router,prefix="/app")

