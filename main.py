from fastapi import FastAPI
from database import engine
import models
from routers import router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Finanzas API")

app.include_router(router)

@app.get("/")
def raiz():
    return {"mensaje": "API de AI Finanzas funcionando"}

@app.get("/salud")
def salud():
    return {"estado": "ok"}