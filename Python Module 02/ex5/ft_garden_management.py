class GardenError(Exception):
    def __str__(self):
        return super().__str__()


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    def __str__(self):
        return "Not enough water in the tank!"


class Plant:
    def __init__(
            self,
            name: str,
            age: int,
            height: int
    ):
        self._name = self.set_name(name)
        self._age = self.set_age(age)
        self._height = self.set_height(height)
        self.days_dry = 5

    def set_name(self, name: str) -> str:
        if not name:
            raise PlantError("Plant name cannot be empty.")
        return name

    def set_age(self, age: int) -> int:
        if age < 0:
            raise PlantError("Plant age cannot be negative.")
        return age

    def set_height(self, height: int) -> int:
        if height <= 0:
            raise PlantError("Plant height must be positive.")
        return height

    def get_name(self) -> str:
        return self._name

    def get_age(self) -> int:
        return self._age

    def get_height(self) -> int:
        return self._height

    def __str__(self):
        return (
            f"Plant(name={self._name}, age={self._age}, "
            f"height={self._height}, days_dry={self.days_dry})"
        )


class GardenManager:
    def __init__(self):
        self._plants = []
        self.water_level = 10

    def add_plant(self, name: str, age: int, height: int):
        try:
            plant = Plant(name, age, height)
            self._plants.append(plant)
        except PlantError as e:
            print(e)
        else:
            print(f"Added {name} successfully")

    def water_plants(self):
        try:
            print("Opening watering system...")
            for plant in self._plants:
                if self.water_level <= 0:
                    raise WaterError()
                print(f"Watering {plant.get_name()}...")
                self.water_level -= 1
                plant.days_dry = 0
            print("All plants watered successfully!")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup).")

    def check_plants(self):
        for plant in self._plants:
            try:
                if plant.days_dry > 7:
                    raise PlantError(f"{plant.get_name()} is wilting!")
            except PlantError as e:
                print(e)
            else:
                print(f"{plant.get_name()}: healthy")

    def get_plants(self):
        return self._plants

    def __getitem__(self, index):
        return self._plants[index]


def test_garden_management():
    print("="*50)
    print("=== Test Garden Management ===")

    manager = GardenManager()

    print("\nAdding plants...")
    manager.add_plant("Rose", 2, 30)
    manager.add_plant("", 3, 25)  # Invalid name
    manager.add_plant("Tulip", -1, 20)  # Invalid age
    manager.add_plant("Daisy", 1, 0)  # Invalid height
    manager.add_plant("Lily", 1, 15)

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    # Simulate days passing
    manager[0].days_dry = 8
    manager.check_plants()

    print("\nAll garden management tests completed!")
    print("="*50)


if __name__ == "__main__":
    test_garden_management()
