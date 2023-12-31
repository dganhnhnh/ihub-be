import random
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class InputSchema(BaseModel):
    no_family_credit_cards: int
    total_electricity_bills_paid_on_time_last_2_years: int
    total_electricity_bills_not_paid_on_time_last_2_years: int
    have_been_laid_off: bool
    have_been_bankrupted: bool
    have_violated_laws: bool
    have_foreclosure: bool
    loan_amounts_overdue_for_30_59_days_last_2_years: int
    loan_amounts_overdue_for_60_89_days_last_2_years: int
    loan_amounts_overdue_for_90_days_above_last_2_years: int
    loan_amounts_paid_on_time_last_2_years: int
    average_family_member_credit_accounts_age: int
    no_new_family_member_credit_accounts_last_2_years: int
    no_family_houses: int
    no_family_members: int
    male: bool
    education_status: str
    marriage_status: str
    tax_in_last_year: int

@app.get("/predict-credit-score")
def predict_credit_score(
    input: InputSchema
) -> float:
    return random.randint(0, 1000)