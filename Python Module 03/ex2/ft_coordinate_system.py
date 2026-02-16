import math
import sys


def calculate_distance(point1: tuple, point2: tuple) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return math.sqrt((x2 - x1) ** 2 +
                     (y2 - y1) ** 2 +
                     (z2 - z1) ** 2)


def parse_coordinates(coord_string: str) -> tuple:
    parts = coord_string.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def demonstrate_unpacking(position: tuple) -> None:
    x, y, z = position
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def validate_args() -> str:
    return sys.argv[1] or "3,4,0"


def main():
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)

    position = (10, 20, 5)
    print("Position created:", position)

    distance = calculate_distance(origin, position)
    print(f"Distance between {origin} and {position}: {round(distance, 2)}")

    coords_str = validate_args()
    print(f'Parsing coordinates: "{coords_str}"')

    try:
        parsed_position = parse_coordinates(coords_str)
        print("Parsed position:", parsed_position)

        distance = calculate_distance(origin, parsed_position)
        print(f"Distance between {origin} and {parsed_position}: {distance}")

    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    invalid_coords = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{invalid_coords}"')

    try:
        parse_coordinates(invalid_coords)

    except ValueError as e:
        print("Error parsing coordinates:", e)
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")

    print("Unpacking demonstration:")
    demonstrate_unpacking((3, 4, 0))


if __name__ == "__main__":
    main()
