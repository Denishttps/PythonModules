from typing import List, Tuple
from ex0 import FlameFactory, AquaFactory
from ex0.factory import CreatureFactory
from ex1 import HealingCreatureFactory, TransformCreatureFactory
from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2.strategy import BattleStrategy


def battle(opponents: List[Tuple[CreatureFactory, BattleStrategy]]) -> None:
    print("*** Tournament ***")
    print(f"{len(opponents)} opponents involved")

    for i in range(len(opponents)):
        for j in range(i + 1, len(opponents)):
            factory1, strategy1 = opponents[i]
            factory2, strategy2 = opponents[j]
            c1 = factory1.create_base()
            c2 = factory2.create_base()
            print()
            print("* Battle *")
            print(c1.describe())
            print(" vs.")
            print(c2.describe())
            print(" now fight!")
            try:
                strategy1.act(c1)
                strategy2.act(c2)
            except ValueError as e:
                print(f"Battle error, aborting tournament: {e}")
                return


if __name__ == "__main__":
    flame_f = FlameFactory()
    aqua_f = AquaFactory()
    heal_f = HealingCreatureFactory()
    trans_f = TransformCreatureFactory()

    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()

    print("Tournament 0 (basic)")
    print("[ (Flameling+Normal), (Healing+Defensive) ]")
    battle([(flame_f, normal), (heal_f, defensive)])

    print()
    print("Tournament 1 (error)")
    print("[ (Flameling+Aggressive), (Healing+Defensive) ]")
    battle([(flame_f, aggressive), (heal_f, defensive)])

    print()
    print("Tournament 2 (multiple)")
    print("[ (Aquabub+Normal), (Healing+Defensive), (Transform+Aggressive) ]")
    battle([(aqua_f, normal), (heal_f, defensive), (trans_f, aggressive)])
