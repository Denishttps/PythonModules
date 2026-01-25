class GardenError(Exception):
    def __str__(self):
        raise NotImplementedError()


class PlantError(GardenError):
    def __str__(self):
        return "The potato plant is wilting!"


class WaterError(GardenError):
    def __str__(self):
        return "Not enough water in the tank!"


def water_plant(water_level):
    if water_level == 0:
        raise WaterError()
    print("Water the plant")
    return water_level - 1


def check_plants(water_level, plants_amount):
    if water_level < plants_amount:
        raise PlantError()
    print("Plants status [OK]")


def main():
    print("="*50)
    print("=== Testing Custom Error ===\n")
    print("Testing WaterError...")
    try:
        water_plant(0)
    except WaterError as e:
        print("Caught", e.__class__.__name__ + ':', e)

    print("\nTesting PlantError...")
    try:
        check_plants(10, 20)
    except PlantError as e:
        print("Caught", e.__class__.__name__ + ':', e)

    print("\nTesting catching all garden errors...")
    try:
        water_plant(0)
    except GardenError as e:
        print("Caught", e.__class__.__name__ + ':', e)

    try:
        check_plants(10, 20)
    except GardenError as e:
        print("Caught", e.__class__.__name__ + ':', e)

    print("\nAll custom error types work correctly!")
    print("="*50)


if __name__ == "__main__":
    main()
