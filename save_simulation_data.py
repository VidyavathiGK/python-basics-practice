import os
from datetime import datetime

def save_simulation_data(filename: str, data: list, header: str = None) -> str:
    """
    Saves a list of data items or simulation results to a specified file.
    
    Args:
        filename (str): The name/path of the file to create.
        data (list): A list of items (numbers, strings, or tuples) to write.
        header (str, optional): Optional header line for the output file.
        
    Returns:
        str: Absolute path of the saved file.
    """
    # Ensure a valid extension if none is provided
    if not os.path.splitext(filename)[1]:
        filename += ".txt"
        
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"# Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            if header:
                file.write(f"{header}\n")
            file.write("-" * 40 + "\n")
            
            for index, item in enumerate(data, start=1):
                file.write(f"{index}: {item}\n")
                
        print(f"Success: Data saved to '{filename}'")
        return os.path.abspath(filename)
    except IOError as e:
        print(f"File Error: Could not write to '{filename}'. Reason: {e}")
        return ""

def main():
    print("=== Simulation & Data Output Saver ===")
    user_filename = input("Enter output file name (e.g., results.txt): ").strip()
    if not user_filename:
        user_filename = "simulation_output.txt"
        
    # Example sample data (e.g., exponential growth or solver steps)
    sample_results = [round(1.5 ** step, 4) for step in range(1, 11)]
    
    save_simulation_data(
        filename=user_filename,
        data=sample_results,
        header="Step | Computed Value"
    )

if __name__ == "__main__":
    main()
