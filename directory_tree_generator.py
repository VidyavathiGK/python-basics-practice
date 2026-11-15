import os

def print_directory_tree(start_path: str, prefix: str = "", ignore_dirs: set = None) -> None:
    """Recursively prints a visual ASCII directory tree of a given folder."""
    if ignore_dirs is None:
        ignore_dirs = {".git", "__pycache__", "node_modules", ".venv"}

    try:
        entries = sorted(os.listdir(start_path))
    except PermissionError:
        print(f"{prefix}[Permission Denied]")
        return

    entries = [e for e in entries if e not in ignore_dirs]
    for index, entry in enumerate(entries):
        full_path = os.path.join(start_path, entry)
        is_last = index == len(entries) - 1
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{entry}")

        if os.path.isdir(full_path):
            extension = "    " if is_last else "│   "
            print_directory_tree(full_path, prefix + extension, ignore_dirs)

if __name__ == "__main__":
    print("=== Directory Tree Generator ===")
    target = input("Enter directory path (leave blank for current folder): ").strip() or "."
    if os.path.exists(target):
        print(f"\n{os.path.abspath(target)}")
        print_directory_tree(target)
    else:
        print("Directory does not exist.")
