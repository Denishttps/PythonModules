from __future__ import annotations

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("durability must be a positive integer")
        if not isinstance(effect, str) or not effect.strip():
            raise ValueError("effect must be a non-empty string")
        self.durability = durability
        self.effect = effect.strip()

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Artifact",
            "durability": self.durability,
            "effect": self.effect,
        })
        return card_info

    def play(self, game_state: dict) -> dict:
        mana_available = game_state.get("mana", 0)
        if not self.is_playable(mana_available):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to deploy artifact",
            }
        artifacts = game_state.setdefault("artifacts", [])
        artifacts.append(self.name)
        game_state["mana"] = mana_available - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": f"Permanent: {self.effect}",
        }

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {
            "artifact": self.name,
            "effect_triggered": self.effect,
            "durability_remaining": max(self.durability, 0),
        }
