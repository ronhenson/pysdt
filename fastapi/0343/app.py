from datetime import datetime
from typing import Any, Dict

from fastapi import FastAPI
from passlib.context import CryptContext
from pydantic import BaseModel

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# We'll explore further in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

AVG_HUMAN_CALORIES_PER_DAY = 2250


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


class User(BaseModel):
    id: int
    username: str
    password: str
    max_daily_calories: int = AVG_HUMAN_CALORIES_PER_DAY

    def __init__(self, **data: Any):
        data["password"] = get_password_hash(data["password"])
        super().__init__(**data)


class FoodEntry(BaseModel):
    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        return self.food.kcal_per_serving * self.number_servings


app = FastAPI()
food_log: Dict[int, FoodEntry] = {}

# To focus on exception handling we only work on Create
# in this Bite hiding read-update-delete endpoints.


@app.post("/", status_code=201)
async def create_food_entry(entry: FoodEntry):

    # TODO: add exception handling code here

    food_log[entry.id] = entry
    return entry