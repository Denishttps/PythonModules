import sys


def main():
    print("=== Command Quest ===")
    args = sys.argv
    if len(args) == 1:
        print("No arguments provided!")
    print("Program name:", args[0])
    if len(args) > 1:
        print("Arguments received:", len(args) - 1)
        i = 1
        while i < len(args):
            print(f"Argument {i}:", args[i])
            i += 1
    print("Total arguments:", len(args))


if __name__ == "__main__":
    main()
