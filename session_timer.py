import time
from contextlib import contextmanager

class SessionTimer:
    """A utility timer for measuring execution time or tracking focus sessions."""
    
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.elapsed_time = 0.0

    def start(self) -> None:
        """Starts the timer."""
        self.start_time = time.time()

    def stop(self) -> float:
        """Stops the timer and returns elapsed seconds."""
        if self.start_time is None:
            raise ValueError("Timer was not started.")
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        return self.elapsed_time

    @contextmanager
    def measure(self, task_name: str = "Task"):
        """Context manager to easily measure block execution time."""
        print(f"[{task_name}] Started...")
        start = time.time()
        try:
            yield
        finally:
            duration = time.time() - start
            print(f"[{task_name}] Completed in {duration:.4f} seconds.")


# --- Example Usage ---
if __name__ == "__main__":
    timer = SessionTimer()
    
    # Using the context manager
    with timer.measure("Heavy Computation Task"):
        total = sum(i**2 for i in range(10_000_000))
    
    print(f"Calculated sum result length: {len(str(total))} digits")
