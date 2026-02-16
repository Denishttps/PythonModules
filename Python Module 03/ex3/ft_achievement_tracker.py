

def main():
    print("=== Achievement Tracker System ===")

    alice = {
        'first_kill',
        'level_10',
        'treasure_hunter',
        'speed_demon'
    }

    bob = {
        'first_kill',
        'level_10',
        'boss_slayer',
        'collector'
    }

    charlie = {
        'level_10',
        'treasure_hunter',
        'boss_slayer',
        'speed_demon',
        'perfectionist'
    }

    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)

    print()
    print("=== Achievement Analytics ===")

    all_achievements = alice.union(bob, charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))

    common = alice.intersection(bob, charlie)
    print("Common to all players:", common)

    alice_rare = alice.difference(bob, charlie)
    bob_rare = bob.difference(alice, charlie)
    charlie_rare = charlie.difference(alice, bob)

    rare = alice_rare.union(bob_rare, charlie_rare)
    print("Rare achievements (1 player):", rare)

    print("Alice vs Bob common:", alice.intersection(bob))
    print("Alice unique:", alice - bob)
    print("Bob unique:", bob - alice)


if __name__ == "__main__":
    main()
