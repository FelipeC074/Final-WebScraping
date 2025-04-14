from fastapi import FastAPI
from app.repositories.DataBase import DBase,Engine
from app.controllers.routes import router
import uvicorn

app = FastAPI()
app.include_router(router=router,prefix="/app")
DBase.metadata.create_all(bind=Engine)

if "__name__" == "Main.py":
    uvicorn.run(app="main:app",reload=True)