import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InputSchema(BaseModel):
    tax_history: float
    electricity_consumption: float
    home_ownership: bool


@app.get("/predict-credit-score")
def predict_credit_score(
    input: InputSchema
) -> float:
    return random.randint(0, 1000)