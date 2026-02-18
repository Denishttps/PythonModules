def read_file(file_name):
    try:
        print(f"CRISIS ALERT: Attempting access to '{file_name}'...")
        with open(file_name) as f:
            print("SUCCESS:", f.read())
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    except Exception as e:
        print("Error:", e)


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    read_file("lost_archive.txt")
    print("STATUS: Crisis handled, system stable\n")

    read_file("classified_vault.txt")
    print("STATUS: Crisis handled, security maintained\n")

    read_file("standard_archive.txt")
    print("STATUS: Normal operations resumed\n")

    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
