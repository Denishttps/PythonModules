import sys


def ft_sum(arr: list[int]) -> int:
    s = 0
    for i in arr:
        s += i
    return s


def ft_min(arr: dict[str, int]) -> int:
    m = float('inf')
    key = ''
    for k, v in arr.items():
        if v < m:
            m = v
            key = k
    return key


def ft_max(arr: dict[str, int]) -> int:
    m = float('-inf')
    key = ''
    for k, v in arr.items():
        if v > m:
            m = v
            key = k
    return key


def validate_arg(arg: str) -> bool:
    try:
        return ":" in arg and int(arg.split(":")[1]) > 0
    except ValueError:
        return False


def parse_args(argv: list[str]) -> dict[str, int]:
    data = {}

    for arg in argv:
        if not validate_arg(arg):
            raise TypeError("Arg should look like <name:str>:<count:int>")
        key, value = arg.split(":")
        data[key] = int(value)
    return data


def print_inventory(inv: dict[str, int], is_stats: bool = True) -> int:
    total_items = ft_sum(inv.values())
    for k, v in inv.items():
        print(
            f"{k}: {v} unit{'s' if v > 1 else ''}"
            f"{f'({v / total_items})' if is_stats else ''}"
        )


def get_scarce(inv: dict[str, int]) -> dict[str, int]:
    scarce_items = {}
    for k, v in inv.items():
        if v < 5:
            scarce_items[k] = v
    return scarce_items


def get_moderate(inv: dict[str, int]) -> dict[str, int]:
    moderate_items = {}
    for k, v in inv.items():
        if v >= 5:
            moderate_items[k] = v
    return moderate_items


def get_restocks(inv: dict[str, int]) -> list[str]:
    lst = []
    for k, v in inv.items():
        if v <= 1:
            lst.append(k)
    return k


def main():
    print("=== Inventory System Analysis ===")

    inventory = parse_args(sys.argv[1:])
    if not inventory:
        return

    total_items = ft_sum(inventory.values())
    print("Total items in inventory:", total_items)
    print("Unique item types:", len(inventory), "\n")

    print("=== Current Inventory ===")
    print_inventory(inventory)

    print()

    print("=== Inventory Statistics ===")
    most_item = ft_max(inventory)
    least_item = ft_min(inventory)
    print(
        "Most abundant:",
        most_item,
        f"({inventory[most_item]} unit"
        f"{'s' if inventory[most_item] > 1 else ''})"
    )
    print(
        "Least abundant:",
        least_item,
        f"({inventory[least_item]} unit"
        f"{'s' if inventory[least_item] > 1 else ''})"
    )

    print()

    print("=== Item Categories ===")
    print("Moderate:", get_moderate(inventory))
    print("Scarce:", get_scarce(inventory))

    print()

    print("=== Management Suggestions ===")
    print("Restock needed:", get_restocks(inventory))

    print()

    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", list(inventory.keys()))
    print("Dictionary values:", list(inventory.values()))
    print(
        "Sample lookup - 'sword' in inventory:",
        bool(inventory.get("sword"))
    )


if __name__ == "__main__":
    main()
