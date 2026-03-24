from __future__ import annotations

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        mana_pool: int,
    ) -> None:
        super().__init__(name, cost, rarity)
        if attack_power <= 0 or health <= 0 or mana_pool < 0:
            raise ValueError("elite card stats must be positive")
        self.attack_power = attack_power
        self.health = health
        self.mana_pool = mana_pool
        self.armor = 3

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Elite",
            "attack": self.attack_power,
            "health": self.health,
            "mana_pool": self.mana_pool,
        })
        return card_info

    def play(self, game_state: dict) -> dict:
        mana_available = game_state.get("mana", 0)
        if not self.is_playable(mana_available):
            return {
                "card_played": self.name,
                "mana_used": 0,
                "effect": "Not enough mana to deploy elite card",
            }
        battlefield = game_state.setdefault("battlefield", [])
        battlefield.append(self.name)
        game_state["mana"] = mana_available - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Elite champion deployed",
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": str(target),
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(self.armor, max(incoming_damage, 0))
        damage_taken = max(incoming_damage - blocked, 0)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
            "armor": self.armor,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_used = min(4, self.mana_pool)
        self.mana_pool -= mana_used
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": list(targets),
            "mana_used": mana_used,
        }

    def channel_mana(self, amount: int) -> dict:
        if amount < 0:
            raise ValueError("amount must be non-negative")
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool,
            "known_spells": ["Fireball", "Shield", "Blink"],
        }
