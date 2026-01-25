def water_plants(plants):
    try:
        print("Opening watering system")
        for plant in plants:
            if not plant:
                raise NameError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    finally:
        print("Closing watering system (cleanup)")
    print("Watering completed successfully!")


def test_watering_system():
    print("="*50)
    print("=== Test finally block in Garden ===")
    currectly_plants = [
        "tomato",
        "potato",
        "carrots"
    ]
    break_plants = currectly_plants[::]
    break_plants[1] = None

    print("Testing normal watering...")
    water_plants(currectly_plants)

    print('')
    print("Testing with error...")
    try:
        water_plants(break_plants)
    except NameError as e:
        print(e)
    finally:
        print("This block is always executed!\n")
    print("Cleanup always happens, even with errors!")
    print("="*50)


if __name__ == "__main__":
    test_watering_system()
