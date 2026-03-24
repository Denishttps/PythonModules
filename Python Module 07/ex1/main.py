from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex1.SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")

    print()

    deck = Deck()
    print("Building deck with different card types...")
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Rare", "damage"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, "Uncommon", 4, "+1 mana per turn"))  # noqa
    deck.shuffle()
    print(f"Deck stats: {deck.get_deck_stats()}")

    print()

    game_state = {"mana": 10, "battlefield": [], "graveyard": [], "artifacts": []}  # noqa
    print("Drawing and playing cards:\n")
    while True:
        try:
            card = deck.draw_card()
        except IndexError:
            break
        print(f"Drew: {card.name} ({card.get_card_info()['type']})")
        print(f"Play result: {card.play(game_state)}")
        print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
