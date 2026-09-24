from datetime import date, datetime

from .charts import create_category_pie_chart
from .service import CATEGORIES, ExpenseService


class ExpenseTrackerCLI:
    def __init__(self):
        self.service = ExpenseService()

    def run(self):
        print("\n=== Smart Expense Tracker ===")
        while True:
            print(
                "\n1. Add expense\n"
                "2. View all expenses\n"
                "3. Monthly summary\n"
                "4. Generate category pie chart\n"
                "5. Delete expense\n"
                "6. Exit"
            )
            choice = input("Choose an option: ").strip()

            try:
                if choice == "1":
                    self.add_expense()
                elif choice == "2":
                    self.view_expenses()
                elif choice == "3":
                    self.monthly_summary()
                elif choice == "4":
                    self.generate_chart()
                elif choice == "5":
                    self.delete_expense()
                elif choice == "6":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid choice.")
            except (ValueError, TypeError) as exc:
                print(f"Error: {exc}")

    def add_expense(self):
        raw_date = input("Date (YYYY-MM-DD, blank=today): ").strip()
        expense_date = date.today() if not raw_date else datetime.strptime(raw_date, "%Y-%m-%d").date()

        print("Categories:", ", ".join(CATEGORIES))
        category = input("Category: ").strip()
        amount = float(input("Amount: ").strip())
        description = input("Description: ").strip()

        expense = self.service.add_expense(expense_date, category, amount, description)
        print(f"Added expense #{expense.expense_id} successfully.")

    def view_expenses(self):
        expenses = self.service.list_expenses()
        if not expenses:
            print("No expenses found.")
            return

        print("\nID   Date         Category          Amount       Description")
        print("-" * 70)
        for e in expenses:
            print(f"{e.expense_id:<4} {e.expense_date}   {e.category:<16} {e.amount:>9.2f}   {e.description}")

    def _get_month(self):
        raw = input("Month (YYYY-MM, blank=current month): ").strip()
        if raw:
            parsed = datetime.strptime(raw, "%Y-%m")
            return parsed.year, parsed.month
        today = date.today()
        return today.year, today.month

    def monthly_summary(self):
        year, month = self._get_month()
        report = self.service.monthly_report(year, month)

        print(f"\n=== Summary: {year}-{month:02d} ===")
        print(f"Total spending: {report['total']:.2f}")

        print("\nCategory breakdown:")
        for category, amount in report["breakdown"].items():
            print(f"  {category:<18} {amount:>10.2f}")

        if report["highest"]:
            print(f"\nHighest spending category: {report['highest'][0]} ({report['highest'][1]:.2f})")

        print("\nInsights:")
        for item in report["insights"]:
            print(f"  - {item}")

    def generate_chart(self):
        year, month = self._get_month()
        report = self.service.monthly_report(year, month)
        if not report["breakdown"]:
            print("No data available for this month.")
            return

        path = f"reports/{year}-{month:02d}_category_breakdown.png"
        create_category_pie_chart(report["breakdown"], path)
        print(f"Chart saved to: {path}")

    def delete_expense(self):
        expense_id = int(input("Enter expense ID to delete: ").strip())
        if self.service.delete_expense(expense_id):
            print("Expense deleted.")
        else:
            print("Expense ID not found.")
