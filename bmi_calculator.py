"""
BMI (Body Mass Index) Calculator
--------------------------------
Calculates BMI using weight and height (supports Metric and Imperial units).
"""

def calculate_bmi_metric(weight_kg, height_m):
    """Calculates BMI using kilograms and meters."""
    return weight_kg / (height_m ** 2)

def calculate_bmi_imperial(weight_lbs, height_in):
    """Calculates BMI using pounds and inches."""
    return (weight_lbs / (height_in ** 2)) * 703

def get_bmi_category(bmi):
    """Returns the standard WHO weight category."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal weight"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("==================================")
    print("        BMI CALCULATOR           ")
    print("==================================")
    print("1. Metric (Kilograms & Meters)")
    print("2. Imperial (Pounds & Inches)")
    
    choice = input("\nSelect system (1 or 2): ").strip()
    
    try:
        if choice == "1":
            weight = float(input("Enter weight in kg: "))
            height = float(input("Enter height in meters: "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be greater than zero.")
                return
            bmi = calculate_bmi_metric(weight, height)
            
        elif choice == "2":
            weight = float(input("Enter weight in pounds (lbs): "))
            height = float(input("Enter height in inches (in): "))
            if weight <= 0 or height <= 0:
                print("Weight and height must be greater than zero.")
                return
            bmi = calculate_bmi_imperial(weight, height)
            
        else:
            print("Invalid choice selected.")
            return
            
        category = get_bmi_category(bmi)
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Category: {category}")
        
    except ValueError:
        print("Please enter valid numeric values.")

if __name__ == "__main__":
    main()
