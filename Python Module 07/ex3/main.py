from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameEngine import GameEngine


def main() -> None:
    print("=== DataDeck Game Engine ===")

    print()

    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print(f"Factory: {factory.__class__.__name__}")
    print(f"Strategy: {strategy.get_strategy_name()}")
    print(f"Available types: {factory.get_supported_types()}")

    print()

    print("Simulating aggressive turn...")
    turn_data = engine.simulate_turn()
    hand_preview = [
        f"{card.name} ({card.cost})"
        for card in turn_data["hand"]
    ]
    print(f"Hand: {hand_preview}")

    print()

    print("Turn execution:")
    print(f"Strategy: {turn_data['strategy']}")
    print(f"Actions: {turn_data['actions']}")

    print()

    print("Game Report:")
    print(engine.get_engine_status())

    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
