def check_temperature(temp_str):
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if temp < 0:
        print(f"Error: {temp_str}°C is too cold for plants (min 0°C)")
    elif temp > 40:
        print(f"Error: {temp_str}°C is too hot for plants (max 40°C)")
    else:
        print(f"Temperature {temp_str}°C is perfect for plants!")


def test_temperature_input():
    test_values = ("25", "abc", "100", "-50")
    try:
        for v in test_values:
            print("Testing temperature:", v)
            check_temperature(v)
            print('')
    except Exception as e:
        print("Test crashed with error:", e)
    finally:
        print("All tests completed - program didn't crash!")


def main():
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()


if __name__ == "__main__":
    main()
