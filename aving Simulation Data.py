def save_results_to_file(filename, data):
    """Saves computation results or logs to a specified file."""
    try:
        with open(filename, "w") as file:
            for item in data:
                file.write(f"{item}\n")
        print(f"Successfully saved results to {filename}")
    except IOError as e:
        print(f"Error writing to file: {e}")

# Example usage:
# results = [0.1, 0.2, 0.4, 0.8, 1.6]
# save_results_to_file("cvode_output.txt", results)
