def analyze_text_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            
            lines = content.splitlines()
            words = content.split()
            characters = len(content)
            
            print(f"--- File Analysis: {filename} ---")
            print(f"Total Lines: {len(lines)}")
            print(f"Total Words: {len(words)}")
            print(f"Total Characters: {characters}")
            
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

if __name__ == "__main__":
    file_name = input("Enter the filename to analyze (e.g., sample.txt): ")
    analyze_text_file(file_name)
