import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n")

    ar_id = input("Input Stream active. Enter archivist ID: ")
    status_msg = input("Input Stream active. Enter status report: ")

    print(
        f"[STANDART] Archive status from {ar_id}: {status_msg}",
        file=sys.stdout
    )
    print(
        "[ALERT] System diagnostic: Communication channels verified",
        file=sys.stderr
    )
    print("[STANDARD] Data transmission complete")

    print()

    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
