class Animal:

    def __init__(self, name: str, age: int, species: str, habitat: str):
        self.name = name
        self.age = age
        self.species = species
        self.habitat = habitat

    def speak(self) -> str:
        # Generic fallback; overridden by child classes.
        return f"{self.name} makes a mysterious sound."

    def birthday(self) -> str:
        self.age += 1
        return f"Happy birthday, {self.name}! You are now {self.age} years old."

    def is_adult(self) -> bool:
        return self.age >= 2

    def describe(self) -> str:
        return f"{self.name} the {self.species} lives in {self.habitat}."

    def __str__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, age={self.age}, species={self.species})"


class Dog(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        habitat: str,
        breed: str,
        favorite_toy: str,
    ):
        super().__init__(name=name, age=age, species="Dog", habitat=habitat)
        self.breed = breed
        self.favorite_toy = favorite_toy

    def speak(self) -> str:
        return f"Woof! {self.name} wants to play with the {self.favorite_toy}."

    def describe(self) -> str:
        base = super().describe()
        return f"{base} Breed: {self.breed}."

    def fetch(self, item: str) -> str:
        return f"{self.name} fetches the {item}!"


class Cat(Animal):
    def __init__(
        self,
        name: str,
        age: int,
        habitat: str,
        color: str,
        prefers_laser: bool,
    ):
        super().__init__(name=name, age=age, species="Cat", habitat=habitat)
        self.color = color
        self.prefers_laser = prefers_laser

    def speak(self) -> str:
        if self.prefers_laser:
            return f"Meow! {self.name} is ready for laser time."
        return f"Mrrp. {self.name} says hello."

    def describe(self) -> str:
        base = super().describe()
        laser_text = "likes lasers" if self.prefers_laser else "doesn't care about lasers"
        return f"{base} Color: {self.color}; {laser_text}."

    def hunt(self, prey: str) -> str:
        return f"{self.name} hunts the {prey} (simulated)!"

