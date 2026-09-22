# unit_converter.py

def convert_length(value, from_unit, to_unit):
    """Converts lengths between meters, kilometers, miles, and feet."""
    # Convert everything to meters first
    to_meters = {
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.34,
        'ft': 0.3048
    }
    
    if from_unit not in to_meters or to_unit not in to_meters:
        raise ValueError("Unsupported unit.")
        
    value_in_meters = value * to_meters[from_unit]
    return value_in_meters / to_meters[to_unit]

if __name__ == "__main__":
    print("=== Length Unit Converter ===")
    try:
        val = float(input("Enter value to convert: "))
        f_unit = input("From unit (m, km, mi, ft): ").strip().lower()
        t_unit = input("To unit (m, km, mi, ft): ").strip().lower()
        
        result = convert_length(val, f_unit, t_unit)
        print(f"\nResult: {val} {f_unit} = {result:.4f} {t_unit}")
    except Exception as e:
        print(f"Error: {e}")
