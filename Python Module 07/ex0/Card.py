from __future__ import annotations

from abc import ABC, abstractmethod
from enum import Enum


class CardType(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"
    ELITE = "Elite"
    TOURNAMENT = "Tournament"


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        if not isinstance(name, str) or not name.strip():
            raise ValueError("name must be a non-empty string")
        if not isinstance(cost, int) or cost < 0:
            raise ValueError("cost must be a non-negative integer")
        if not isinstance(rarity, str) or not rarity.strip():
            raise ValueError("rarity must be a non-empty string")
        self.name = name.strip()
        self.cost = cost
        self.rarity = rarity.strip()

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        raise NotImplementedError

    def get_card_type(self) -> str:
        class_name = self.__class__.__name__
        if class_name.endswith("Card"):
            class_name = class_name[:-4]
        return class_name

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity,
            "type": self.get_card_type(),
        }

    def is_playable(self, available_mana: int) -> bool:
        if not isinstance(available_mana, int):
            return False
        return available_mana >= self.cost
