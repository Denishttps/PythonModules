from __future__ import annotations

import random

from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("deck can only store Card instances")
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for index, card in enumerate(self.cards):
            if card.name == card_name:
                del self.cards[index]
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if not self.cards:
            raise IndexError("cannot draw from an empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        total_cost = sum(card.cost for card in self.cards)
        return {
            "total_cards": total_cards,
            "creatures": sum(
                1 for card in self.cards if card.get_card_info()["type"] == "Creature"  # noqa
            ),
            "spells": sum(
                1 for card in self.cards if card.get_card_info()["type"] == "Spell"  # noqa
            ),
            "artifacts": sum(
                1 for card in self.cards if card.get_card_info()["type"] == "Artifact"  # noqa
            ),
            "avg_cost": round(total_cost / total_cards, 2) if total_cards else 0.0,  # noqa
        }
