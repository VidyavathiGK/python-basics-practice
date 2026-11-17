import json
import os

def compare_json_files(file1: str, file2: str) -> dict:
    """Compares two JSON files and reports added, removed, and modified keys."""
    try:
        with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
            data1 = json.load(f1)
            data2 = json.load(f2)
    except Exception as e:
        print(f"Error reading files: {e}")
        return {}

    keys1, keys2 = set(data1.keys()), set(data2.keys())
    
    added = keys2 - keys1
    removed = keys1 - keys2
    common = keys1 & keys2
    
    modified = {k for k in common if data1[k] != data2[k]}

    return {
        "added_keys": list(added),
        "removed_keys": list(removed),
        "modified_keys": list(modified)
    }

if __name__ == "__main__":
    print("=== JSON Data Differ Utility ===")
    d1 = {"theme": "dark", "version": 1.0, "debug": False}
    d2 = {"theme": "light", "version": 1.1, "debug": False, "plugins": []}
    
    with open("v1.json", "w") as f1, open("v2.json", "w") as f2:
        json.dump(d1, f1)
        json.dump(d2, f2)

    diff = compare_json_files("v1.json", "v2.json")
    print("Comparison Result:", diff)
