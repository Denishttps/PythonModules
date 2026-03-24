from __future__ import annotations

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(
        self,
        card_id: str,
        name: str,
        cost: int,
        rarity: str,
        attack_power: int,
        health: int,
        rating: int = 1200,
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(card_id, str) or not card_id.strip():
            raise ValueError("card_id must be a non-empty string")
        if attack_power <= 0 or health <= 0:
            raise ValueError("tournament stats must be positive")
        self.card_id = card_id
        self.attack_power = attack_power
        self.health = health
        self.rating = rating
        self.wins = 0
        self.losses = 0

    def get_card_info(self) -> dict:
        card_info = super().get_card_info()
        card_info.update({
            "type": "Tournament",
            "card_id": self.card_id,
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
                "effect": "Not enough mana for tournament deployment",
            }
        game_state["mana"] = mana_available - self.cost
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Tournament combatant enters the arena",
        }

    def attack(self, target) -> dict:
        target_name = getattr(target, "name", str(target))
        return {
            "attacker": self.name,
            "target": target_name,
            "damage": self.attack_power,
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(incoming_damage, 0)
        self.health -= damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack": self.attack_power,
            "health": self.health,
        }

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins
        self.rating += wins * 16

    def update_losses(self, losses: int) -> None:
        self.losses += losses
        self.rating -= losses * 16

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
        }

    def get_tournament_stats(self) -> dict:
        return {
            "id": self.card_id,
            "name": self.name,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}",
            "combat": self.get_combat_stats(),
        }
