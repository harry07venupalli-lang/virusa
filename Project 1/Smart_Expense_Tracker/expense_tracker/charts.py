from pathlib import Path
from typing import Dict

import matplotlib.pyplot as plt


def create_category_pie_chart(breakdown: Dict[str, float], output_path: str):
    if not breakdown:
        raise ValueError("No category data available for chart.")

    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    labels = list(breakdown.keys())
    values = list(breakdown.values())

    plt.figure(figsize=(8, 6))
    plt.pie(values, labels=labels, autopct="%1.1f%%", startangle=90)
    plt.title("Expense Breakdown by Category")
    plt.tight_layout()
    plt.savefig(output, dpi=150)
    plt.close()

    return output
