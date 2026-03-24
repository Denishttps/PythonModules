from __future__ import annotations

from ex0.Card import Card


class CreatureCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        health: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(attack, int) or attack <= 0:
            raise ValueError("attack must be a positive integer")
        if not isinstance(health, int) or health <= 0:
            raise ValueError("health must be a positive integer")
        self.attack_power = attack
        self.health = health

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Creature",
            "attack": self.attack_power,
            "health": self.health,
        })
        return card_info

    def play(self, game_state: dict) -> dict:
        mana_available = game_state.get("mana", 0)
        if not self.is_playable(mana_available):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to summon creature",
            }
        battlefield = game_state.setdefault("battlefield", [])
        battlefield.append(self.name)
        game_state["mana"] = mana_available - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield",
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage_dealt": self.attack_power,
            "combat_resolved": True,
        }
