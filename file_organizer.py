import os
import shutil

# Define the dictionary mapping folder categories to their file extensions
EXTENSION_MAPPING = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".json", ".sql"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Audio_Video": [".mp3", ".wav", ".mp4", ".mkv", ".avi", ".mov"],
    "Executables": [".exe", ".dmg", ".pkg", ".deb"],
}


def organize_folder(target_directory):
  """Scans the target directory and moves files into categorized subfolders."""
  if not os.path.exists(target_directory):
    print(f"\n[Error] The directory '{target_directory}' does not exist.")
    return

  print(f"\nScanning directory: {target_directory}...\n")
  files_moved = 0

  # Iterate through all items in the target directory
  for filename in os.listdir(target_directory):
    file_path = os.path.join(target_directory, filename)

    # Skip directories, only process files
    if os.path.isdir(file_path):
      continue

    # Get the file extension in lowercase
    _, ext = os.path.splitext(filename)
    ext = ext.lower()

    if not ext:
      continue  # Skip files with no extension

    # Find which category this extension belongs to
    assigned_category = "Others"
    for category, extensions in EXTENSION_MAPPING.items():
      if ext in extensions:
        assigned_category = category
        break

    # Create the category subfolder if it doesn't already exist
    category_folder = os.path.join(target_directory, assigned_category)
    if not os.path.exists(category_folder):
      os.makedirs(category_folder)

    # Move the file to the category subfolder
    destination_path = os.path.join(category_folder, filename)

    # Handle duplicate file names gracefully by appending a suffix if needed
    base_name, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(destination_path):
      new_filename = f"{base_name}_{counter}{extension}"
      destination_path = os.path.join(category_folder, new_filename)
      counter += 1

    try:
      shutil.move(file_path, destination_path)
      print(f"Moved: {filename} ---> {assigned_category}/")
      files_moved += 1
    except Exception as e:
      print(f"Failed to move {filename}: {e}")

  print("\n" + "=" * 40)
  print(f" Organization complete! Total files sorted: {files_moved}")
  print("=" * 40 + "\n")


def main():
  print("--- Automated File Organizer ---")
  path = input(
      "Enter the full path of the folder you want to organize (or press Enter"
      " for current folder): "
  ).strip()

  if not path:
    path = os.getcwd()

  confirm = (
      input(
          f"Are you sure you want to organize files in '{path}'? (y/n): "
      )
      .strip()
      .lower()
  )
  if confirm == "y":
    organize_folder(path)
  else:
    print("Operation cancelled.")


if __name__ == "__main__":
  main()
