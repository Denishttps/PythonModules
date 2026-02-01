class Plant:
    def __init__(self, name: str, height: int, age: int):
        self.name = name
        self.height = height
        self.age = age

    def __str__(self):
        return f"{self.name}: {self.height}cm, {self.age} days old"


def main():
    print("=== Garden Plant Registry ===")
    my_plants = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 100)
    ]
    for plant in my_plants:
        print(plant)


if __name__ == "__main__":
    main()
