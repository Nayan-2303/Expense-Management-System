from fastapi import FastAPI, HTTPException
from datetime import date
import db_helper
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Expense(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date


class MonthYear(BaseModel):
    month: int  # e.g., 8 for August
    year: int   # e.g., 2024



@app.get("/expenses/{expense_date}", response_model=List[Expense])
def get_expenses(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    if expenses is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expenses from the database.")

    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expense(expense_date: date, expenses:List[Expense]):
    db_helper.delete_expenses_for_date(expense_date)
    for expense in expenses:
        db_helper.insert_expense(expense_date, expense.amount, expense.category, expense.notes)

    return {"message": "Expenses updated successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db_helper.fetch_expenses_summary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    return breakdown

# Backend endpoint (FastAPI)
@app.post("/analytics_by_month/")
def get_analytics(month_year: MonthYear):
    # Fetch the monthly data from the database
    data = db_helper.fetch_expenses_by_month(month_year.month, month_year.year)

    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")

    # Calculate the total expense for the month
    total_expense = sum([row['total'] for row in data])

    # Calculate breakdown by category with percentage
    breakdown = {}
    for row in data:
        percentage = (row['total'] / total_expense) * 100 if total_expense != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }

    # Include the total expense in the response
    response = {
        "total_expense": total_expense,
        "breakdown": breakdown
    }

    return response
