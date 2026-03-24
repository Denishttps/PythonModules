from ex2.EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")

    print()

    elite = EliteCard("Arcane Warrior", 4, "Epic", 5, 8, 8)

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    print()

    print("Playing Arcane Warrior (Elite Card):\n")

    print("Combat phase:")
    print(f"Attack result: {elite.attack('Enemy')}")
    print(f"Defense result: {elite.defend(5)}")

    print()

    print("Magic phase:")
    print(
        "Spell cast: "
        f"{elite.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}"
    )
    print(f"Mana channel: {elite.channel_mana(3)}")

    print()

    print("Multiple interface implementation successful!")


if __name__ == "__main__":
    main()
