# Smart Expense Tracker

A beginner-friendly Python CLI project that records expenses, stores them in CSV, produces monthly summaries, analyzes category spending, detects the highest spending category, and generates a pie chart.

## Features

- Add expenses with date, category, amount, and description
- CSV-based persistent storage
- View all saved expenses
- Monthly expense summary
- Category-wise spending breakdown
- Highest spending category detection
- Simple spending insights
- Matplotlib pie chart
- Delete expenses
- Automated unit tests
- Sample data included

## Project Structure

```text
smart_expense_tracker/
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── expenses.csv
├── reports/
│   └── .gitkeep
├── expense_tracker/
│   ├── __init__.py
│   ├── models.py
│   ├── storage.py
│   ├── analytics.py
│   ├── charts.py
│   ├── service.py
│   └── cli.py
└── tests/
    └── test_analytics.py
```

## Requirements

- Python 3.10+
- matplotlib

## Installation

### Windows

```powershell
cd smart_expense_tracker
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### macOS/Linux

```bash
cd smart_expense_tracker
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python main.py
```

You will get a menu:

1. Add expense
2. View all expenses
3. Monthly summary
4. Generate category pie chart
5. Delete expense
6. Exit

## Generate the chart

Choose option 4 and enter a month such as:

```text
2026-09
```

The chart is saved under:

```text
reports/2026-09_category_breakdown.png
```

## Run tests

```bash
python -m unittest discover -s tests -v
```

## Example insight

For a month where Food is the largest category, the application may report:

- Highest spending category: Food
- Average daily spending
- Food represents a large percentage of total spending
- Review the category if it exceeds 40% of monthly spending

## Design

The project separates responsibilities:

- `models.py` — data model
- `storage.py` — CSV persistence
- `analytics.py` — calculations and insights
- `charts.py` — visualization
- `service.py` — application/business logic
- `cli.py` — user interface
- `main.py` — entry point

This makes the project easy to extend later with a GUI, SQLite database, budgets, login, export, or a web interface.
