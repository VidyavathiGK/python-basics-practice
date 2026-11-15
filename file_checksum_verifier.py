import hashlib
import os

def calculate_file_hash(filepath: str, algorithm: str = "sha256") -> str:
    """Computes cryptographic hash (MD5, SHA1, SHA256) of a file in chunks."""
    if not os.path.isfile(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    hasher = hashlib.new(algorithm)
    with open(filepath, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def verify_checksum(filepath: str, expected_hash: str, algorithm: str = "sha256") -> bool:
    """Compares calculated file hash against an expected checksum."""
    actual_hash = calculate_file_hash(filepath, algorithm)
    return actual_hash.lower() == expected_hash.strip().lower()

if __name__ == "__main__":
    print("=== File Checksum Verifier ===")
    path = input("Enter file path to hash: ").strip()
    try:
        digest = calculate_file_hash(path, "sha256")
        print(f"SHA-256: {digest}")
    except Exception as e:
        print(f"Error: {e}")
