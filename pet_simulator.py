class Pet:
    def __init__(self, name, species, sound):
        self.name = name
        self.species = species
        self.sound = sound
        self.is_adopted = False

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def adopt(self):
        if not self.is_adopted:
            self.is_adopted = True
            return f"Congratulations! You have successfully adopted {self.name} the {self.species}."
        return f"{self.name} has already been adopted."

# Creating objects (instantiation)
pet1 = Pet("Buddy", "Dog", "Woof")
pet2 = Pet("Whiskers", "Cat", "Meow")

# Interacting with the objects
print(pet1.speak())          # Output: Buddy says Woof!
print(pet2.adopt())          # Output: Congratulations! You have successfully adopted Whiskers the Cat.
print(pet2.adopt())          # Output: Whiskers has already been adopted.
print(f"Is {pet1.name} adopted? {pet1.is_adopted}") # Output: Is Buddy adopted? False
