# Smart Expense Tracker — Project Report

## 1. Introduction

The Smart Expense Tracker is a Python-based command-line application designed to help users record and understand their daily expenses. It stores expense records in CSV format and provides monthly analytics and visualizations.

## 2. Objectives

1. Record daily expenses.
2. Categorize spending.
3. Store data persistently.
4. Generate monthly summaries.
5. Display category-wise spending.
6. Identify the highest spending category.
7. Provide simple spending insights.
8. Visualize spending using a pie chart.

## 3. Technologies Used

- Python
- CSV
- Dataclasses
- Matplotlib
- unittest

## 4. Functional Modules

### Expense Model
Represents an expense using date, category, amount, description, and ID.

### Storage Module
Reads and writes expenses to `data/expenses.csv`.

### Analytics Module
Calculates:
- total spending
- category totals
- highest spending category
- average daily spending
- basic insights

### Chart Module
Creates a category-wise pie chart using Matplotlib.

### CLI Module
Provides the interactive menu through the terminal.

## 5. Program Flow

```text
Start
  |
  v
Display Menu
  |
  +--> Add Expense --> Validate --> Save CSV
  |
  +--> View Expenses --> Read CSV --> Display
  |
  +--> Monthly Summary --> Filter Month --> Analyze --> Display
  |
  +--> Generate Chart --> Analyze --> Matplotlib --> Save PNG
  |
  +--> Delete Expense --> Remove Record --> Save CSV
  |
  +--> Exit
```

## 6. Data Format

The CSV contains:

| Field | Description |
|---|---|
| id | Unique expense identifier |
| date | Expense date |
| category | Spending category |
| amount | Expense amount |
| description | Short explanation |

## 7. Example

Suppose a user records:

- Food: 250
- Travel: 120
- Bills: 800
- Shopping: 450
- Entertainment: 300

The application calculates the total, ranks category totals internally, identifies the largest category, and can generate a pie chart.

## 8. Testing

Unit tests cover:
- total expense calculation
- category breakdown
- highest spending category

Run:

```bash
python -m unittest discover -s tests -v
```

## 9. Future Enhancements

Possible improvements include:

- Tkinter GUI
- SQLite database
- Monthly budget limits
- CSV/Excel export
- Login and multiple users
- Search and filtering
- Line chart for spending trends
- Budget alerts
- Recurring expenses
- PDF reports
- Web version using Flask or Streamlit

## 10. Conclusion

The project satisfies the core requirements of a Smart Expense Tracker while keeping the architecture simple enough for a student Python project. The modular structure also provides a foundation for future development.
