

def main():
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    print(
        "Initiating secure vault access..."
        "Vault connection established with failsafe protocols\n"
    )

    print("SECURE EXTRACTION:")
    with open("classified_data.txt") as f:
        print(f.read())
        print()

    print("SECURE PRESERVATION:")
    with open("security_protocols.txt") as f:
        print(f.read())
        print()

    print(
        "Vault automatically sealed upon completion"
        "All vault operations completed with maximum security."
    )


if __name__ == "__main__":
    main()
