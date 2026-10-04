import time
import sys


def countdown(minutes, label):
  """Countdown timer for a given number of minutes."""
  total_seconds = minutes * 60
  print(f"\n--- Starting {label} ({minutes} mins) ---")

  while total_seconds > 0:
    mins, secs = divmod(total_seconds, 60)
    timer_display = f"{mins:02d}:{secs:02d}"
    
    # Print timer inline using carriage return
    sys.stdout.write(f"\r[{label}] Time remaining: {timer_display} ")
    sys.stdout.flush()
    
    time.sleep(1)
    total_seconds -= 1

  print(f"\n[{label}] Time's up! 🎉")


def pomodoro_timer():
  """Runs the Pomodoro technique cycle: Work -> Short Break -> Long Break."""
  print("=" * 45)
  print("         POMODORO TIMER WORKFLOW")
  print("=" * 45)
  
  try:
    work_mins = int(input("Enter work duration in minutes (default 25): ") or 25)
    short_break_mins = int(input("Enter short break duration in minutes (default 5): ") or 5)
    long_break_mins = int(input("Enter long break duration in minutes (default 15): ") or 15)
    cycles = int(input("Enter number of work cycles before a long break (default 4): ") or 4)
  except ValueError:
    print("Invalid input. Using default Pomodoro settings (25/5/15 mins, 4 cycles).")
    work_mins, short_break_mins, long_break_mins, cycles = 25, 5, 15, 4

  for current_cycle in range(1, cycles + 1):
    print(f"\n*** Cycle {current_cycle} of {cycles} ***")
    
    # Work session
    countdown(work_mins, "Work Session")

    if current_cycle < cycles:
      # Short break
      countdown(short_break_mins, "Short Break")
    else:
      # Long break after finishing all cycles
      countdown(long_break_mins, "Long Break")

  print("\n" + "=" * 45)
  print(" All Pomodoro cycles completed! Great job today! 🚀")
  print("=" * 45 + "\n")


if __name__ == "__main__":
  pomodoro_timer()
