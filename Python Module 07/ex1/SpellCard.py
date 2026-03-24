from __future__ import annotations

from ex0.Card import Card


class SpellCard(Card):
    VALID_EFFECTS = {
        "damage": "Deal 3 damage to target",
        "heal": "Restore 3 health to target",
        "buff": "Grant +2 attack to ally",
        "debuff": "Reduce enemy power by 2",
    }

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
    ) -> None:
        super().__init__(name, cost, rarity)
        if effect_type not in self.VALID_EFFECTS:
            raise ValueError("effect_type must be damage, heal, buff, or debuff")  # noqa
        self.effect_type = effect_type

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Spell",
            "effect_type": self.effect_type,
        })
        return card_info

    def play(self, game_state: dict) -> dict:
        mana_available = game_state.get("mana", 0)
        if not self.is_playable(mana_available):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to cast spell",
            }
        graveyard = game_state.setdefault("graveyard", [])
        graveyard.append(self.name)
        game_state["mana"] = mana_available - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.VALID_EFFECTS[self.effect_type],
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell": self.name,
            "effect_type": self.effect_type,
            "targets": list(targets),
            "resolved": True,
        }
