import unittest
from datetime import date

from expense_tracker.analytics import (
    category_breakdown,
    highest_spending_category,
    total_expenses,
)
from expense_tracker.models import Expense


class TestAnalytics(unittest.TestCase):
    def setUp(self):
        self.expenses = [
            Expense(date(2026, 9, 1), "Food", 100, "Lunch", 1),
            Expense(date(2026, 9, 2), "Travel", 50, "Bus", 2),
            Expense(date(2026, 9, 3), "Food", 150, "Dinner", 3),
        ]

    def test_total(self):
        self.assertEqual(total_expenses(self.expenses), 300)

    def test_breakdown(self):
        self.assertEqual(category_breakdown(self.expenses)["Food"], 250)

    def test_highest_category(self):
        self.assertEqual(highest_spending_category(self.expenses), ("Food", 250))


if __name__ == "__main__":
    unittest.main()
