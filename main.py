from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Sheep Compendium!"}
from fastapi import HTTPException
from models.db import db
from models.models import Sheep

@app.get("/sheep/{sheep_id}", response_model=Sheep)
def get_sheep(sheep_id: int):
    sheep = db.get_sheep(sheep_id)
    if sheep is None:
        raise HTTPException(status_code=404, detail="Sheep not found")
    return sheep
from fastapi import status

@app.post("/sheep", status_code=status.HTTP_201_CREATED)
def add_sheep(sheep: Sheep):
    db.add_sheep(sheep)
    return sheep
