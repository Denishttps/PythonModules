import sys


def args_validation(args: list[str]) -> list[int]:
    result = []
    for elem in args:
        try:
            result.append(int(elem))
        except ValueError:
            print(f"{elem} is not integer")
            raise SystemExit()
    return result


def main():
    print("=== Player Score Analytics ===")
    argv = args_validation(sys.argv[1:])
    if not argv:
        print(
            "No scores provided. Usage: python3 ft_score_analytics.py "
            "<score1> <score2> ..."
        )
        return
    print("Scores processed:", argv)
    print("Total players:", len(argv))
    print("Total score:", sum(argv))
    print("Average score:", sum(argv) / len(argv))
    print("High score:", max(argv))
    print("Low score:", min(argv))
    print("Score range:", max(argv) - min(argv))


if __name__ == "__main__":
    main()
