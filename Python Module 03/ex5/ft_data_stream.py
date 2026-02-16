from typing import Generator


EVENTS = [
  {"name": "player1", "level": 3, "type": "killed_monster"},
  {"name": "player2", "level": 7, "type": "found_treasure"},
  {"name": "player3", "level": 5, "type": "leveled_up"},
  {"name": "player4", "level": 12, "type": "killed_monster"},
  {"name": "player5", "level": 9, "type": "found_treasure"},
  {"name": "player6", "level": 15, "type": "leveled_up"},
  {"name": "player7", "level": 4, "type": "killed_monster"},
  {"name": "player8", "level": 18, "type": "found_treasure"},
  {"name": "player9", "level": 6, "type": "leveled_up"},
  {"name": "player10", "level": 10, "type": "killed_monster"},
  {"name": "player11", "level": 2, "type": "found_treasure"},
  {"name": "player12", "level": 14, "type": "leveled_up"},
  {"name": "player13", "level": 8, "type": "killed_monster"},
  {"name": "player14", "level": 11, "type": "found_treasure"},
  {"name": "player15", "level": 16, "type": "leveled_up"},
  {"name": "player16", "level": 1, "type": "killed_monster"},
  {"name": "player17", "level": 19, "type": "found_treasure"},
  {"name": "player18", "level": 13, "type": "leveled_up"},
  {"name": "player19", "level": 7, "type": "killed_monster"},
  {"name": "player20", "level": 5, "type": "found_treasure"},
  {"name": "player21", "level": 9, "type": "leveled_up"},
  {"name": "player22", "level": 6, "type": "killed_monster"},
  {"name": "player23", "level": 17, "type": "found_treasure"},
  {"name": "player24", "level": 3, "type": "leveled_up"},
  {"name": "player25", "level": 12, "type": "killed_monster"},
  {"name": "player26", "level": 8, "type": "found_treasure"},
  {"name": "player27", "level": 4, "type": "leveled_up"},
  {"name": "player28", "level": 15, "type": "killed_monster"},
  {"name": "player29", "level": 10, "type": "found_treasure"},
  {"name": "player30", "level": 18, "type": "leveled_up"},
  {"name": "player31", "level": 2, "type": "killed_monster"},
  {"name": "player32", "level": 14, "type": "found_treasure"},
  {"name": "player33", "level": 6, "type": "leveled_up"},
  {"name": "player34", "level": 11, "type": "killed_monster"},
  {"name": "player35", "level": 9, "type": "found_treasure"},
  {"name": "player36", "level": 16, "type": "leveled_up"},
  {"name": "player37", "level": 1, "type": "killed_monster"},
  {"name": "player38", "level": 19, "type": "found_treasure"},
  {"name": "player39", "level": 13, "type": "leveled_up"},
  {"name": "player40", "level": 7, "type": "killed_monster"},
  {"name": "player41", "level": 5, "type": "found_treasure"},
  {"name": "player42", "level": 9, "type": "leveled_up"},
  {"name": "player43", "level": 6, "type": "killed_monster"},
  {"name": "player44", "level": 17, "type": "found_treasure"},
  {"name": "player45", "level": 3, "type": "leveled_up"},
  {"name": "player46", "level": 12, "type": "killed_monster"},
  {"name": "player47", "level": 8, "type": "found_treasure"},
  {"name": "player48", "level": 4, "type": "leveled_up"},
  {"name": "player49", "level": 15, "type": "killed_monster"},
  {"name": "player50", "level": 10, "type": "found_treasure"}
]


def event_generator(events: list) -> Generator[list, None, None]:
    for event in events:
        yield event


def print_stats() -> None:
    total_events = 0
    hight_level = 0
    treasure_events = 0
    level_up_events = 0
    for event in event_generator(EVENTS):
        total_events += 1
        if event["level"] > 9:
            hight_level += 1
        if event["type"] == "found_treasure":
            treasure_events += 1
        elif event["type"] == "leveled_up":
            level_up_events += 1

    print("Total events processed:", total_events)
    print("High-level players (10+):", hight_level)
    print("Treasure events:", treasure_events)
    print("Level-up events:", level_up_events)
    print("Memory usage: Constant (streaming)")


def fibonachi() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator():
    i = 2
    while True:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                break
        else:
            yield i
        i += 1


def main():
    print("=== Game Data Stream Processor ===")
    print("Processing 50 game events...")
    events = event_generator(EVENTS)
    for i in range(len(EVENTS)):
        print(f"Event {i+1}: {next(events)}")

    print("\n=== Stream Analytics ===")
    print_stats()

    print()

    print("=== Generator Demonstration ===")
    print("Fibonacci sequence (first 20): ", end="")
    for i in fibonachi():
        if i == 4181:
            print(f"{i}")
            break
        print(f"{i}, ", end="")

    print("Prime numbers (first 10): ", end="")
    for i in prime_generator():
        if i == 29:
            print(f"{i}")
            break
        print(f"{i}, ", end="")


if __name__ == "__main__":
    main()
