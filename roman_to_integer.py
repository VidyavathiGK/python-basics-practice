"""
Roman Numeral to Integer Converter
----------------------------------
Converts a given Roman numeral string into its integer value.
"""

def roman_to_int(s: str) -> int:
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    
    total = 0
    n = len(s)
    
    for i in range(n):
        current_value = roman_map.get(s[i].upper(), 0)
        
        # If the current value is less than the next value, subtract it (e.g., IV = 4)
        if i + 1 < n and current_value < roman_map.get(s[i + 1].upper(), 0):
            total -= current_value
        else:
            total += current_value
            
    return total

def main():
    print("==================================")
    print("   ROMAN NUMERAL TO INTEGER      ")
    print("==================================")
    
    while True:
        roman = input("\nEnter a Roman numeral (or type 'quit' to exit): ").strip()
        if roman.lower() == 'quit':
            break
            
        try:
            result = roman_to_int(roman)
            print(f"The integer value of {roman.upper()} is: {result}")
        except KeyError:
            print("Invalid Roman numeral characters entered. Try again.")

if __name__ == "__main__":
    main()
