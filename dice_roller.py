import random

def roll_dice():
    print("--- Dice Roller Simulator ---")
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? (Enter 0 to quit): "))
            if num_dice == 0:
                print("Exiting Dice Roller. Goodbye!")
                break
            if num_dice < 0:
                print("Please enter a positive number.")
                continue
                
            rolls = [random.randint(1, 6) for _ in range(num_dice)]
            print(f"Results: {rolls}")
            print(f"Total Sum: {sum(rolls)}\n")
            
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    roll_dice()
