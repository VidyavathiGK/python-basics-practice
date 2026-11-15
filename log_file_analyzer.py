import re
from collections import Counter

def analyze_log_file(filepath: str) -> dict:
    """
    Parses a standard log file and counts occurrences of log levels
    (INFO, WARNING, ERROR, CRITICAL) along with the top error messages.
    """
    level_counts = Counter()
    error_messages = Counter()
    log_pattern = re.compile(r"\b(INFO|WARNING|ERROR|CRITICAL)\b[:\s-]+(.*)")

    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                match = log_pattern.search(line)
                if match:
                    level, message = match.groups()
                    level_counts[level] += 1
                    if level in ("ERROR", "CRITICAL"):
                        error_messages[message.strip()] += 1
    except FileNotFoundError:
        print(f"Error: Log file '{filepath}' not found.")
        return {}

    return {
        "levels": dict(level_counts),
        "top_errors": error_messages.most_common(5)
    }

if __name__ == "__main__":
    print("=== Log File Analyzer ===")
    path = input("Enter log file path (e.g., app.log): ").strip()
    report = analyze_log_file(path)
    if report:
        print("\nLog Level Summary:", report["levels"])
        print("Top Errors:")
        for err, count in report["top_errors"]:
            print(f"  - [{count}x] {err}")
