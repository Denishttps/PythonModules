

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age
        self._on_create()

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self, days):
        self.height += days

    def age(self, days):
        self.plant_age += days

    def _on_create(self):
        print(
            f"Created: {self.name} ({self.height}cm, {self.plant_age} days)"
        )


def main():
    print("=== Plant Factory Output ===")
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Sunflower", 80, 45),
        ("Cactus", 5, 90),
        ("Fern", 15, 120)
    ]
    plants = []
    for data in plants_data:
        plant = Plant(*data)
        plants.append(plant)

    print(f"\nTotal plants created: {len(plants)}")


if __name__ == "__main__":
    main()
