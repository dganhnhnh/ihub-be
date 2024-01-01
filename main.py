import random
import csv
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InputSchema(BaseModel):
    numberOfFamilyCreditCards: int
    totalElectricityBillsPaidOnTimeLast2Years: int
    totalElectricityBillsNotPaidOnTimeLast2Years: int
    haveBeenLaidOff: bool
    haveBeenBankrupted: bool
    haveViolatedLaws: bool
    haveForeclosure: bool
    loanAmountsOverdueFor3059DaysInTheLast2Years: int
    loanAmountsOverdueFor6089DaysInTheLast2Years: int
    loanAmountsOverdueFor90DaysInTheLast2Years: int
    numberOfLoanPaidOnTimeInTheLast2Years: int
    averageFamilyMemberCreditAccountsAge: int
    numberOfNewFamilyMemberCreditAccountsInTheLast2Years: int
    numberOfFamilyHouses: int
    numberOfFamilyMembers: int
    gender: bool
    educationStatus: str
    marriageStatus: str
    taxInTheLastlYear: int

    
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


@app.get("/predict-credit-score")
def predict_credit_score(
    input: InputSchema
) -> float:
    return random.randint(0, 1000)