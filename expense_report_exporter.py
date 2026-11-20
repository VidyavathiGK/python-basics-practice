import csv
from collections import defaultdict


def summarize_by_category(transactions: list[dict]) -> dict[str, float]:
    """Aggregates total amounts per category from a list of {'category': ..., 'amount': ...} dicts."""
    totals: dict[str, float] = defaultdict(float)
    for tx in transactions:
        category = str(tx.get("category", "Uncategorized")).strip() or "Uncategorized"
        amount = float(tx.get("amount", 0.0))
        totals[category] += amount
    return dict(totals)


def export_summary_csv(summary: dict[str, float], output_path: str = "expense_summary.csv") -> str:
    """Writes category totals and overall total to a CSV file."""
    grand_total = sum(summary.values())
    with open(output_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Category", "Total Amount"])
        for category, total in sorted(summary.items()):
            writer.writerow([category, f"{total:.2f}"])
        writer.writerow(["TOTAL", f"{grand_total:.2f}"])
    return output_path


if __name__ == "__main__":
    sample_tx = [
        {"category": "Food", "amount": 18.50},
        {"category": "Transport", "amount": 12.00},
        {"category": "Food", "amount": 9.25},
        {"category": "Utilities", "amount": 65.00},
    ]
    summary = summarize_by_category(sample_tx)
    saved_file = export_summary_csv(summary)
    print("Summary:", summary)
    print("Saved report to:", saved_file)
