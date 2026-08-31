class SmartBulb:
    def __init__(self, room):
        self.room = room
        self.is_on = False
        self.brightness = 50

    def turn_on(self):
        self.is_on = True
        return f"The {self.room} bulb is now ON."

    def turn_off(self):
        self.is_on = False
        return f"The {self.room} bulb is now OFF."

    def set_brightness(self, level):
        if self.is_on:
            self.brightness = max(0, min(100, level))
            return f"{self.room} brightness set to {self.brightness}%."
        return f"Turn on the {self.room} bulb first."

# Creating an object
living_room_light = SmartBulb("Living Room")

# Interacting with the object
print(living_room_light.turn_on())           # Output: The Living Room bulb is now ON.
print(living_room_light.set_brightness(75))  # Output: Living Room brightness set to 75%.
print(living_room_light.turn_off())          # Output: The Living Room bulb is now OFF.
