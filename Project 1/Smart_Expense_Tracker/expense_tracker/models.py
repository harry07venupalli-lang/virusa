from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class Expense:
    expense_date: date
    category: str
    amount: float
    description: str = ""
    expense_id: Optional[int] = None

    def to_dict(self) -> dict:
        return {
            "id": self.expense_id,
            "date": self.expense_date.isoformat(),
            "category": self.category,
            "amount": f"{self.amount:.2f}",
            "description": self.description,
        }
