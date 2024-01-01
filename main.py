import random
import csv
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
    "http://144.126.242.191:2999"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputSchema(BaseModel):
    loan_type: str
    loan_value: float
    collateral_value: float
    identity_number: int

    
@app.get("/get-info")
def get_info() -> dict:
    csv_file_path = './data.csv'

    with open(csv_file_path, 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

    header = rows[0]
    data = rows[1:]
    rr = random.choice(data)
    rd = dict(zip(header, rr))
    # rd without creditStatus attribute
    del rd['creditStatus']
    return rd


@app.post("/predict-loan-probability")
def predict_loan_probability(
    input: InputSchema
) -> float:
    if input.collateral_value > 2*input.loan_value:
        return 84.27
    elif input.collateral_value > input.loan_value:
        return 68.20
    elif input.collateral_value < 0.5*input.loan_value:
        return 20.15
    else:
        return 35.89