from __future__ import annotations

from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard
from ex3.CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.creatures = {
            "dragon": ("Fire Dragon", 5, "Legendary", 7, 5),
            "goblin": ("Goblin Warrior", 2, "Common", 2, 2),
        }
        self.spells = {
            "fireball": ("Fireball", 4, "Rare", "damage"),
            "lightning": ("Lightning Bolt", 3, "Rare", "damage"),
        }
        self.artifacts = {
            "mana_ring": ("Mana Ring", 2, "Uncommon", 5, "+1 mana per turn"),
            "crystal": ("Arcane Crystal", 3, "Rare", 4, "+2 spell power"),
        }

    def create_creature(self, name_or_power: str | int | None = None):
        key = "dragon" if name_or_power in (None, "dragon", 7) else "goblin"
        return CreatureCard(*self.creatures[key])

    def create_spell(self, name_or_power: str | int | None = None):
        key = "fireball" if name_or_power in (None, "fireball", 4) else "lightning"  # noqa
        return SpellCard(*self.spells[key])

    def create_artifact(self, name_or_power: str | int | None = None):
        key = (
            "mana_ring"
            if name_or_power in (None, "mana_ring", 2)
            else "crystal"
        )
        return ArtifactCard(*self.artifacts[key])

    def create_themed_deck(self, size: int) -> dict:
        cards = []
        builders = [
            self.create_creature("dragon"),
            self.create_creature("goblin"),
            self.create_spell("lightning"),
            self.create_artifact("mana_ring"),
        ]
        while len(cards) < size:
            template = builders[len(cards) % len(builders)]
            cards.append(template)
        return {"theme": "Fantasy", "size": size, "cards": cards}

    def get_supported_types(self) -> dict:
        return {
            "creatures": list(self.creatures.keys()),
            "spells": list(self.spells.keys()),
            "artifacts": list(self.artifacts.keys()),
        }
