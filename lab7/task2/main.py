from models import Animal, Cat, Dog


def main() -> None:
    # Create instances from each class.
    animals = [
        Animal(name="Mystery", age=1, species="Creature", habitat="an old forest"),
        Dog(
            name="Buddy",
            age=3,
            habitat="a sunny yard",
            breed="Golden Retriever",
            favorite_toy="rubber ball",
        ),
        Cat(
            name="Whiskers",
            age=2,
            habitat="a cozy apartment",
            color="gray",
            prefers_laser=True,
        ),
    ]

    # Iterate over objects in a list and call shared methods.
    for animal in animals:
        print(animal)  # __str__
        print(animal.describe())
        print(animal.speak())  # polymorphism: Dog/Cat override this
        print(f"Is adult? {animal.is_adult()}")
        print("-" * 60)

    # Call methods unique to child classes.
    for animal in animals:
        if isinstance(animal, Dog):
            print(animal.fetch("newspaper"))
        elif isinstance(animal, Cat):
            print(animal.hunt("toy mouse"))


if __name__ == "__main__":
    main()

