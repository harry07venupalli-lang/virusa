import csv
from datetime import date
from pathlib import Path
from typing import List

from .models import Expense


class CSVStorage:
    """Simple CSV persistence layer for expenses."""

    FIELDNAMES = ["id", "date", "category", "amount", "description"]

    def __init__(self, file_path: str = "data/expenses.csv"):
        self.file_path = Path(file_path)
        self.file_path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_file()

    def _ensure_file(self):
        if not self.file_path.exists():
            with self.file_path.open("w", newline="", encoding="utf-8") as f:
                csv.DictWriter(f, fieldnames=self.FIELDNAMES).writeheader()

    def load(self) -> List[Expense]:
        expenses = []
        with self.file_path.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if not row.get("date"):
                    continue
                expenses.append(
                    Expense(
                        expense_date=date.fromisoformat(row["date"]),
                        category=row["category"],
                        amount=float(row["amount"]),
                        description=row.get("description", ""),
                        expense_id=int(row["id"]) if row.get("id") else None,
                    )
                )
        return expenses

    def save_all(self, expenses: List[Expense]):
        with self.file_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=self.FIELDNAMES)
            writer.writeheader()
            for expense in expenses:
                writer.writerow(expense.to_dict())

    def add(self, expense: Expense) -> Expense:
        expenses = self.load()
        next_id = max((e.expense_id or 0 for e in expenses), default=0) + 1
        expense.expense_id = next_id
        expenses.append(expense)
        self.save_all(expenses)
        return expense

    def delete(self, expense_id: int) -> bool:
        expenses = self.load()
        remaining = [e for e in expenses if e.expense_id != expense_id]
        if len(remaining) == len(expenses):
            return False
        self.save_all(remaining)
        return True
