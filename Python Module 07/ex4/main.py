from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("=== DataDeck Tournament Platform ===")

    print()

    print("Registering Tournament Cards...")

    platform = TournamentPlatform()
    dragon = TournamentCard("dragon_001", "Fire Dragon", 5, "Legendary", 7, 5)
    wizard = TournamentCard("wizard_001", "Ice Wizard", 4, "Epic", 5, 4, 1150)

    for card in (dragon, wizard):
        print()
        platform.register_card(card)
        print(f"{card.name} (ID: {card.card_id}):")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print(f"- Record: {card.wins}-{card.losses}")

    print()

    print("Creating tournament match...")
    print(f"Match result: {platform.create_match('dragon_001', 'wizard_001')}")

    print()

    print("Tournament Leaderboard:")
    leaderboard = platform.get_leaderboard()
    for index, entry in enumerate(leaderboard, start=1):
        print(
            f"{index}. {entry['name']} - Rating: {entry['rating']} "
            f"({entry['record']})"
        )

    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())

    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
