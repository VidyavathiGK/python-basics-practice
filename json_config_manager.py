import json
import os

class JSONConfigManager:
    def __init__(self, filename: str = "config.json"):
        self.filename = filename
        self.config = self.load_config()

    def load_config(self) -> dict:
        """Loads configuration from JSON file or provides default values."""
        default_config = {"theme": "dark", "auto_save": True, "max_retries": 3}
        if not os.path.exists(self.filename):
            self.save_config(default_config)
            return default_config
        
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Corrupted config file found. Resetting to defaults.")
            return default_config

    def save_config(self, data: dict = None) -> None:
        """Saves current configuration state to disk."""
        target = data if data is not None else self.config
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(target, f, indent=4)

    def update_setting(self, key: str, value) -> None:
        """Updates a specific configuration key and persists it."""
        self.config[key] = value
        self.save_config()
        print(f"Updated setting: '{key}' -> {value}")

if __name__ == "__main__":
    manager = JSONConfigManager("app_config.json")
    manager.update_setting("theme", "light")
    manager.update_setting("timeout", 45)
