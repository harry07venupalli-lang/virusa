from collections import defaultdict
from datetime import date
from typing import Dict, List

from .models import Expense


def filter_month(expenses: List[Expense], year: int, month: int) -> List[Expense]:
    return [e for e in expenses if e.expense_date.year == year and e.expense_date.month == month]


def total_expenses(expenses: List[Expense]) -> float:
    return round(sum(e.amount for e in expenses), 2)


def category_breakdown(expenses: List[Expense]) -> Dict[str, float]:
    totals = defaultdict(float)
    for expense in expenses:
        totals[expense.category] += expense.amount
    return {k: round(v, 2) for k, v in sorted(totals.items(), key=lambda x: -x[1])}


def highest_spending_category(expenses: List[Expense]):
    breakdown = category_breakdown(expenses)
    return max(breakdown.items(), key=lambda x: x[1]) if breakdown else None


def average_daily_spending(expenses: List[Expense], year: int, month: int) -> float:
    days = date(year, month + 1, 1) if month < 12 else date(year + 1, 1, 1)
    first = date(year, month, 1)
    day_count = (days - first).days
    return round(total_expenses(expenses) / day_count, 2) if day_count else 0.0


def insights(expenses: List[Expense], year: int, month: int) -> List[str]:
    if not expenses:
        return ["No expenses recorded for this month."]

    result = []
    total = total_expenses(expenses)
    top = highest_spending_category(expenses)

    if top:
        category, amount = top
        percentage = (amount / total * 100) if total else 0
        result.append(
            f"Highest spending category: {category} ({amount:.2f}, {percentage:.1f}% of total)."
        )

    avg = average_daily_spending(expenses, year, month)
    result.append(f"Average daily spending for the month: {avg:.2f}.")

    if top and total and top[1] / total >= 0.40:
        result.append(
            f"{top[0]} accounts for at least 40% of monthly spending; review it for possible savings."
        )

    if total > 0:
        result.append("Tip: set a monthly target and compare actual spending against it.")

    return result
