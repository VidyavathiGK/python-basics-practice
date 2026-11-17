import time
from functools import wraps

class RateLimiter:
    """A token-bucket or time-window based rate limiter for function execution."""
    def __init__(self, max_calls: int, period_seconds: float):
        self.max_calls = max_calls
        self.period_seconds = period_seconds
        self.calls = []

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            # Remove timestamps outside the current time window
            self.calls = [t for t in self.calls if now - t < self.period_seconds]
            
            if len(self.calls) >= self.max_calls:
                sleep_time = self.period_seconds - (now - self.calls[0])
                print(f"Rate limit reached for '{func.__name__}'. Waiting {sleep_time:.2f}s...")
                time.sleep(sleep_time)
                now = time.time()
                self.calls = [t for t in self.calls if now - t < self.period_seconds]

            self.calls.append(now)
            return func(*args, **kwargs)
        return wrapper

if __name__ == "__main__":
    limiter = RateLimiter(max_calls=2, period_seconds=3.0)

    @limiter
    def fetch_api_data(endpoint: str):
        print(f"Fetching data from {endpoint} at {time.strftime('%X')}")

    print("Testing Rate Limiter:")
    fetch_api_data("/users")
    fetch_api_data("/posts")
    fetch_api_data("/settings")  # This should trigger the delay
