import csv
import os

def clean_csv_data(input_file: str, output_file: str) -> None:
    """Reads a CSV file, removes rows with missing primary fields, and outputs a clean file."""
    if not os.path.exists(input_file):
        print(f"Error: File '{input_file}' not found.")
        return

    rows = []
    with open(input_file, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if not header:
            print("Error: CSV file is empty.")
            return
        
        for row in reader:
            # Drop rows with empty fields
            if row and all(field.strip() for field in row):
                rows.append(row)

    # Remove duplicates
    unique_rows = [list(x) for x in set(tuple(row) for row in rows)]

    with open(output_file, mode="w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(unique_rows)

    print(f"Success! Cleaned data saved to '{output_file}'. Total rows saved: {len(unique_rows)}")

if __name__ == "__main__":
    print("=== CSV Data Cleaner ===")
    inp = input("Enter source CSV file name: ").strip()
    out = input("Enter output CSV file name: ").strip() or "cleaned_output.csv"
    clean_csv_data(inp, out)
