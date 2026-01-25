def ft_seed_inventory(seed_type: str, quant: int, unit: str) -> None:
    seed_type_formated = seed_type.capitalize()
    match unit:
        case "packets":
            print(
                f"{seed_type_formated} seeds: {quant} packets available"
            )
        case "grams":
            print(
                f"{seed_type_formated} seeds: {quant} grams total"
            )
        case "area":
            print(
                f"{seed_type_formated} seeds: covers {quant} square meters"
            )
