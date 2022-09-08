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
