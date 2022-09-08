from typing import Dict

from fastapi import FastAPI
from pydantic import BaseModel


class Food(BaseModel):
    """Model from Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


app = FastAPI()
foods: Dict[int, Food] = {}


# write the Create endpoint
@app.post("/", response_model=foods, status_code=201)
async def create_foods(food: Food):
    foods[food.id] = food
    return food
