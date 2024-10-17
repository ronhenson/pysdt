from typing import Dict

from pydantic import BaseModel

# write a Food pydantic model
class Food(BaseModel):
    """ Using pydantic to define a Food model"""
    id : int
    name : str
    serving_size : str
    kcal_per_serving : int
    protein_grams : float
    fibre_grams : float = 0

if __name__ == "__main__":
    food = (Food(
        id=1,
        name="egg",
        serving_size="piece",
        kcal_per_serving=78,
        protein_grams=6.3,
        fibre_grams=0,
    ))
    print(food.id, food.name)

    print(f'food in total = {food}')
    foods:  Dict[int, Food] = {}
    foods[food.id] = Food
    print("foods dictionary:", food.json())
