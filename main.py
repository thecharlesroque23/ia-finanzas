from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def raiz():
    return {"mensaje": "API de AI Finanzas funcionando"}

@app.get("/salud")
def salud():
    return {"estado": "ok"}
