from __future__ import annotations

from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0

    def configure_engine(
        self,
        factory: CardFactory,
        strategy: GameStrategy,
    ) -> None:
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> dict:
        if self.factory is None or self.strategy is None:
            raise RuntimeError("engine must be configured before simulation")

        hand = [
            self.factory.create_creature("dragon"),
            self.factory.create_creature("goblin"),
            self.factory.create_spell("lightning"),
        ]
        battlefield: list[str] = []
        result = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.cards_created += len(hand)
        self.total_damage += result["damage_dealt"]
        return {
            "strategy": self.strategy.get_strategy_name(),
            "hand": hand,
            "actions": result,
        }

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            strategy_name = "Unconfigured"
        else:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
