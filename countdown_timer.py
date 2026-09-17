import time

def countdown(seconds):
    print(f"--- Countdown Timer Started for {seconds} seconds ---")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer_display = f"{mins:02d}:{secs:02d}"
        print(timer_display, end="\r")
        time.sleep(1)
        seconds -= 1
        
    print("\nTime's up! ⏰")

if __name__ == "__main__":
    try:
        user_time = int(input("Enter time in seconds for the countdown: "))
        countdown(user_time)
    except ValueError:
        print("Please enter a valid integer for seconds.")
