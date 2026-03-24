from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===\n")
    print("Testing Abstract Base Class Design:\n")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)
    print("CreatureCard Info:\n")
    print(fire_dragon.get_card_info())

    print()

    playable_state = {"mana": 6, "battlefield": []}
    print("Playing Fire Dragon with 6 mana available:")
    print(f"Playable: {fire_dragon.is_playable(playable_state['mana'])}")
    print(f"Play result: {fire_dragon.play(playable_state)}")

    print()

    print("Fire Dragon attacks Goblin Warrior:")
    print(f"Attack result: {fire_dragon.attack_target('Goblin Warrior')}")

    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {fire_dragon.is_playable(3)}")

    print()

    try:
        Card("Broken Blueprint", 1, "Common")
    except TypeError as error:
        print(f"Cannot instantiate Card directly: {error}")

    print()

    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
