# updated code
class CSVParser:
    def __init__(self, csv_string):
        lines = csv_string.strip().split("\n")
        self.headers = [h.strip() for h in lines[0].split(",")]
        self.rows = []
        for line in lines[1:]:
            values = [v.strip() for v in line.split(",")]
            self.rows.append(dict(zip(self.headers, values)))

    def filter_by(self, column, value):
        return [row for row in self.rows if row.get(column) == value]

# Example usage:
if __name__ == "__main__":
    data = """
    name, role, department
    Alice, Developer, Engineering
    Bob, Designer, UI/UX
    Charlie, Developer, Engineering
    """
    parser = CSVParser(data)
    developers = parser.filter_by("role", "Developer")
    print("\n--- Filtered Developers --- ")
    for dev in developers:
        print(dev["name"])
