import time
from typing import Optional

class RateLimiter:
    """A simple time-interval rate limiter to restrict operation frequency."""
    
    def __init__(self, max_calls: int, period_seconds: float):
        self.max_calls = max_calls
        self.period_seconds = period_seconds
        self.call_timestamps: list[float] = []

    def allow_request(self) -> bool:
        """Determines if a new operation is permitted based on the time window."""
        current_time = time.time()
        
        # Remove timestamps older than our time window
        self.call_timestamps = [
            t for t in self.call_timestamps 
            if current_time - t < self.period_seconds
        ]
        
        # Check if we have room for another call
        if len(self.call_timestamps) < self.max_calls:
            self.call_timestamps.append(current_time)
            return True
            
        return False

    def time_until_next_slot(self) -> float:
        """Returns seconds remaining until a new call slot opens up."""
        if len(self.call_timestamps) < self.max_calls:
            return 0.0
        oldest_call = self.call_timestamps[0]
        elapsed = time.time() - oldest_call
        return max(0.0, self.period_seconds - elapsed)


# --- Example Usage ---
if __name__ == "__main__":
    # Allow a maximum of 3 calls per 2 seconds
    limiter = RateLimiter(max_calls=3, period_seconds=2.0)
    
    for i in range(5):
        allowed = limiter.allow_request()
        print(f"Request {i+1}: Allowed? {allowed}")
        if not allowed:
            print(f" -> Rate limited! Wait {limiter.time_until_next_slot():.2f}s")
        time.sleep(0.4)
