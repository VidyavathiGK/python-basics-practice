from collections import OrderedDict
from typing import Any, Optional

class LRUCache:
    """A Least Recently Used (LRU) cache with fixed capacity."""
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: str) -> Optional[Any]:
        """Retrieves an item and marks it as recently used."""
        if key not in self.cache:
            return None
        # Move to end to show it was recently accessed
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: str, value: Any) -> None:
        """Inserts or updates a key-value pair, evicting the oldest item if capacity is exceeded."""
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        
        if len(self.cache) > self.capacity:
            # Pop the first item (the least recently used one)
            evicted_key, _ = self.cache.popitem(last=False)
            print(f"Capacity reached. Evicted LRU item: '{evicted_key}'")


# --- Example Usage ---
if __name__ == "__main__":
    cache = LRUCache(capacity=2)
    cache.put("a", 1)
    cache.put("b", 2)
    print("Get 'a':", cache.get("a"))  # Accesses 'a', making 'b' the least recently used
    
    cache.put("c", 3)  # Should evict 'b'
    print("Get 'b' (should be None):", cache.get("b"))
    print("Get 'c':", cache.get("c"))
