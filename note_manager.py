import datetime
import os

NOTE_FILE = "my_notes.txt"

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    note_entry = f"\n--- {title} ({timestamp}) ---\n{content}\n"
    
    with open(NOTE_FILE, "a") as f:
        f.write(note_entry)
    print("Note saved successfully!")

def view_notes():
    if not os.path.exists(NOTE_FILE):
        print("No notes found.")
        return
        
    print("\n=== Your Saved Notes ===")
    with open(NOTE_FILE, "r") as f:
        print(f.read())

if __name__ == "__main__":
    while True:
        print("\n1. Add Note\n2. View Notes\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            break
        else:
            print("Invalid option. Try again.")
