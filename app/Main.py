from fastapi import FastAPI
import pandas as pd
import controllers.routes as rts

app = FastAPI()
app.include_router(router=rts.router,prefix="/app")


