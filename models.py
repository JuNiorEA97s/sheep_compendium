from pydantic import BaseModel

class Sheep(BaseModel):
    id: int
    name: str
    breed: str
    age: int
    sex: str
