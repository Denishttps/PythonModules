

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")

    try:
        with open("ancient_fragment.txt") as file:
            print("Connection established...\n")
            print(file.read())
            print()
    except FileNotFoundError:
        print("Error: Fragment not found in storage.")
    except Exception as e:
        print("Error:", e)

    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    main()
