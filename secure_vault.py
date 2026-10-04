import base64
import getpass
import hashlib
import os
import sqlite3
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

DB_NAME = "vault.db"
SALT_FILE = "vault.salt"


def generate_key(master_password, salt):
  """Derives a secure encryption key from the master password using PBKDF2."""
  kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=100_000,
  )
  key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
  return key


def init_db(master_password):
  """Initializes the SQLite database and stores the master password hash."""
  if not os.path.exists(SALT_FILE):
    salt = os.urandom(16)
    with open(SALT_FILE, "wb") as f:
      f.write(salt)
  else:
    with open(SALT_FILE, "rb") as f:
      salt = f.read()

  # Hash the master password to verify it on future logins
  pwd_hash = hashlib.sha256(master_password.encode()).hexdigest()

  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()

  cursor.execute("""
        CREATE TABLE IF NOT EXISTS vault (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            service TEXT UNIQUE NOT NULL,
            username TEXT NOT NULL,
            encrypted_password TEXT NOT NULL
        )
    """)

  # Store or check master metadata table
  cursor.execute("""
        CREATE TABLE IF NOT EXISTS metadata (
            id INTEGER PRIMARY KEY,
            master_hash TEXT NOT NULL
        )
    """)

  cursor.execute("SELECT master_hash FROM metadata WHERE id = 1")
  row = cursor.fetchone()

  if row is None:
    cursor.execute(
        "INSERT INTO metadata (id, master_hash) VALUES (1, ?)", (pwd_hash,)
    )
    conn.commit()
  elif row[0] != pwd_hash:
    conn.close()
    raise ValueError("Incorrect master password!")

  conn.close()
  return salt


def add_credential(service, username, password, cipher_suite):
  """Encrypts and stores a new username/password pair."""
  encrypted_pwd = cipher_suite.encrypt(password.encode()).decode()

  try:
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO vault (service, username, encrypted_password) VALUES (?, ?,"
        " ?)",
        (service.lower(), username, encrypted_pwd),
    )
    conn.commit()
    print(f"\n[Success] Credentials for '{service}' saved securely!")
  except sqlite3.IntegrityError:
    print(f"\n[Error] Service '{service}' already exists in the vault.")
  finally:
    conn.close()


def get_credential(service, cipher_suite):
  """Retrieves and decrypts credentials for a given service."""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute(
      "SELECT username, encrypted_password FROM vault WHERE service = ?",
      (service.lower(),),
  )
  row = cursor.fetchone()
  conn.close()

  if row:
    username, encrypted_pwd = row
    decrypted_pwd = cipher_suite.decrypt(encrypted_pwd.encode()).decode()
    print("\n" + "=" * 30)
    print(f" Service  : {service}")
    print(f" Username : {username}")
    print(f" Password : {decrypted_pwd}")
    print("=" * 30)
  else:
    print(f"\n[Error] No credentials found for '{service}'.")


def list_services():
  """Lists all saved services in the vault."""
  conn = sqlite3.connect(DB_NAME)
  cursor = conn.cursor()
  cursor.execute("SELECT service FROM vault")
  services = cursor.fetchall()
  conn.close()

  if services:
    print("\nStored Services in Vault:")
    for s in services:
      print(f"- {s[0].capitalize()}")
  else:
    print("\nYour vault is currently empty.")


def main():
  print("--- Secure Password Vault ---")
  master_pass = getpass.getpass("Enter your Master Password: ")

  try:
    salt = init_db(master_pass)
    key = generate_key(master_pass, salt)
    cipher_suite = Fernet(key)
  except ValueError as e:
    print(f"\n[Access Denied] {e}")
    return

  while True:
    print("\nMenu:")
    print("1. Add/Update Credential")
    print("2. Retrieve Credential")
    print("3. List All Services")
    print("4. Exit")

    choice = input("Choose an option (1-4): ").strip()

    if choice == "1":
      service = input("Enter service name (e.g., github): ").strip()
      username = input("Enter username/email: ").strip()
      password = getpass.getpass("Enter password to store: ")
      add_credential(service, username, password, cipher_suite)

    elif choice == "2":
      service = input("Enter service name to retrieve: ").strip()
      get_credential(service, cipher_suite)

    elif choice == "3":
      list_services()

    elif choice == "4":
      print("Exiting vault. Stay secure!")
      break
    else:
      print("Invalid choice. Please select between 1 and 4.")


if __name__ == "__main__":
  main()
