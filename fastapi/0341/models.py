from datetime import datetime
import pwd
from typing import Any

from passlib.context import CryptContext
from pydantic import BaseModel, validator

# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
# which we'll further explore in a later Bite
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password):
    return pwd_context.hash(password)


class Food(BaseModel):
    """Bite 02"""

    id: int
    name: str
    serving_size: str
    kcal_per_serving: int
    protein_grams: float
    fibre_grams: float = 0


# Write the User and FoodEntry models here ...

class User(BaseModel):
    """User attributes Bite 341"""

    id: int
    username: str
    password: str

    @validator("password")
    def hash_password(cls, pw):
        return get_password_hash(pw)


class FoodEntry(BaseModel):
    """Food entry atrributes Bite 341"""

    id: int
    user: User
    food: Food
    date_added: datetime = datetime.now()
    number_servings: float

    @property
    def total_calories(self):
        """Calculate total kilocalories"""
        return self.number_servings * self.food.kcal_per_serving
