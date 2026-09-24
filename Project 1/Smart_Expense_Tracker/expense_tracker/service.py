from datetime import date
from typing import List

from .analytics import (
    category_breakdown,
    filter_month,
    highest_spending_category,
    insights,
    total_expenses,
)
from .models import Expense
from .storage import CSVStorage


CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Health", "Education", "Entertainment", "Other"]


class ExpenseService:
    def __init__(self, storage: CSVStorage | None = None):
        self.storage = storage or CSVStorage()

    def add_expense(self, expense_date: date, category: str, amount: float, description: str):
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        category = category.strip().title()
        if not category:
            raise ValueError("Category cannot be empty.")
        return self.storage.add(
            Expense(expense_date, category, round(amount, 2), description.strip())
        )

    def list_expenses(self) -> List[Expense]:
        return sorted(self.storage.load(), key=lambda e: (e.expense_date, e.expense_id or 0), reverse=True)

    def monthly_report(self, year: int, month: int):
        month_expenses = filter_month(self.storage.load(), year, month)
        breakdown = category_breakdown(month_expenses)
        return {
            "expenses": month_expenses,
            "total": total_expenses(month_expenses),
            "breakdown": breakdown,
            "highest": highest_spending_category(month_expenses),
            "insights": insights(month_expenses, year, month),
        }

    def delete_expense(self, expense_id: int) -> bool:
        return self.storage.delete(expense_id)
