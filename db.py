from models.models import Sheep
class FakeDB:
    def __init__(self):
        self.sheep_data = {
            1: {"id": 1, "name": "Spice", "breed": "Gotland", "age": 3, "sex": "Female"},
        }

    def get_sheep(self, sheep_id: int):
        return self.sheep_data.get(sheep_id)

db = FakeDB()
def add_sheep(self, sheep: Sheep):
    self.sheep_data[sheep.id] = sheep.dict()
