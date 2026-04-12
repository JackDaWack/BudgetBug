from pydantic import BaseModel
from fastapi import APIRouter

router = APIRouter()

class income_data(BaseModel):
    amount: int
    source: str

class expense_data(BaseModel):
    amount: int
    category: str

class BudgetProfile:
    def __init__(self, user_id):
        self.user_id = user_id
        self.incomes = {}
        self.expenses = {}
    def add_income(self, amount, source):
        if source in self.incomes:
            self.incomes[source] += amount
        else:
            self.incomes[source] = amount
    def add_expense(self, amount, category):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount

@router.post("/add-income")
def add_income(data: income_data):
    pass

@router.post("/add-expense")
def add_expenses(data: expense_data):
    pass
