def convert_temperature():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit & Kelvin")
    print("2. Fahrenheit to Celsius & Kelvin")
    print("3. Kelvin to Celsius & Fahrenheit")
    
    choice = input("Choose an option (1-3): ")
    
    try:
        if choice == "1":
            c = float(input("Enter temperature in Celsius: "))
            f = (c * 9/5) + 32
            k = c + 273.15
            print(f"{c}°C = {f:.2f}°F and {k:.2f}K")
        elif choice == "2":
            f = float(input("Enter temperature in Fahrenheit: "))
            c = (f - 32) * 5/9
            k = c + 273.15
            print(f"{f}°F = {c:.2f}°C and {k:.2f}K")
        elif choice == "3":
            k = float(input("Enter temperature in Kelvin: "))
            c = k - 273.15
            f = (c * 9/5) + 32
            print(f"{k}K = {c:.2f}°C and {f:.2f}°F")
        else:
            print("Invalid choice selected.")
    except ValueError:
        print("Please enter a valid numeric value.")

if __name__ == "__main__":
    convert_temperature()
