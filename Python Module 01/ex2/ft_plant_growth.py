

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.plant_age = age

    def get_info(self):
        print(f"{self.name}: {self.height}cm, {self.plant_age} days old")

    def grow(self, days):
        self.height += days

    def age(self, days):
        self.plant_age += days


def main():
    print("=== Day 1 ===")
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height
    rose.get_info()

    print("=== Day 7 ===")
    rose.grow(6)
    rose.age(6)
    rose.get_info()
    growth = rose.height - initial_height
    print(f"Growth this week: +{growth}cm")


if __name__ == "__main__":
    main()
