import json
import os
import time
from typing import Any, Dict, Optional

class JSONCacheManager:
    """A simple file-based cache manager with TTL support."""
    
    def __init__(self, cache_filepath: str = "local_cache.json"):
        self.cache_filepath = cache_filepath
        self._cache: Dict[str, Dict[str, Any]] = self._load_cache()

    def _load_cache(self) -> Dict[str, Dict[str, Any]]:
        """Loads cache data from disk."""
        if not os.path.exists(self.cache_filepath):
            return {}
        try:
            with open(self.cache_filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}

    def _save_cache(self) -> None:
        """Persists cache data to disk."""
        try:
            with open(self.cache_filepath, "w", encoding="utf-8") as f:
                json.dump(self._cache, f, indent=4)
        except Exception as e:
            print(f"Error saving cache: {e}")

    def set(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        """Sets a cache value with an optional expiration time in seconds."""
        expiry = time.time() + ttl_seconds if ttl_seconds else None
        self._cache[key] = {
            "value": value,
            "expiry": expiry
        }
        self._save_cache()

    def get(self, key: str) -> Optional[Any]:
        """Retrieves a cached item if it exists and hasn't expired."""
        if key not in self._cache:
            return None
        
        item = self._cache[key]
        if item["expiry"] and time.time() > item["expiry"]:
            # Expired, clean up
            del self._cache[key]
            self._save_cache()
            return None
            
        return item["value"]


# --- Example Usage ---
if __name__ == "__main__":
    cache = JSONCacheManager("test_cache.json")
    
    # Cache data with a 5-second TTL
    cache.set("user_session", {"username": "Vidyavathi", "role": "developer"}, ttl_seconds=5)
    
    print("Immediate retrieval:", cache.get("user_session"))
