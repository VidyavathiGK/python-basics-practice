def generate_markdown_table(headers: list, rows: list) -> str:
    """Generates a well-formatted Markdown table string from headers and rows."""
    if not headers or not rows:
        return "Invalid data provided for table."

    # Calculate maximum width for each column to ensure clean alignment
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val)))

    # Format header row
    header_str = "| " + " | ".join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + " |"
    
    # Format divider row
    divider_str = "| " + " | ".join("-" * col_widths[i] for i in range(len(headers))) + " |"

    # Format data rows
    row_strs = []
    for row in rows:
        row_strs.append("| " + " | ".join(str(val).ljust(col_widths[i]) for i, val in enumerate(row)) + " |")

    return "\n".join([header_str, divider_str] + row_strs)

if __name__ == "__main__":
    headers = ["Project File", "Category", "Status"]
    rows = [
        ["save_simulation_data.py", "Utilities", "Completed"],
        ["csv_data_cleaner.py", "Data Processing", "Ready"],
        ["json_config_manager.py", "System", "Ready"]
    ]
    
    print("=== Generated Markdown Table ===")
    print(generate_markdown_table(headers, rows))
