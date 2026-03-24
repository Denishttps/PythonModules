from __future__ import annotations

from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        sorted_hand = sorted(hand, key=lambda card: (card.cost, card.name))
        cards_played: list[str] = []
        mana_used = 0
        damage_dealt = 0

        for card in sorted_hand:
            if isinstance(card, CreatureCard) and mana_used + card.cost <= 5:
                battlefield.append(card.name)
                cards_played.append(card.name)
                mana_used += card.cost
                damage_dealt += card.attack_power
            elif isinstance(card, SpellCard) and card.effect_type == "damage":
                if mana_used + card.cost <= 5:
                    cards_played.append(card.name)
                    mana_used += card.cost
                    damage_dealt += 3

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return sorted(available_targets, key=lambda target: str(target))
