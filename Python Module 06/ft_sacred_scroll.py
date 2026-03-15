

def directly_imports():
    import alchemy.elements

    try:
        fire = alchemy.elements.create_fire()
        water = alchemy.elements.create_water()
        earth = alchemy.elements.create_earth()
        air = alchemy.elements.create_air()
        print("alchemy.elements.create_fire(): ", fire)
        print("alchemy.elements.create_water(): ", water)
        print("alchemy.elements.create_earth(): ", earth)
        print("alchemy.elements.create_air(): ", air)
    except Exception as e:
        print(f"Error: {e}")


def package_level_imports():
    import alchemy

    try:
        fire = alchemy.create_fire()
        water = alchemy.create_water()
        earth = alchemy.create_earth()
        air = alchemy.create_air()
        print("alchemy.create_fire(): ", fire)
        print("alchemy.create_water(): ", water)
        print("alchemy.create_earth(): ", earth)
        print("alchemy.create_air(): ", air)
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access: ")
    directly_imports()

    print()

    print("Testing package-level access (controlled by __init__.py): ")
    package_level_imports()

    import alchemy
    print()

    print("Package metadata: ")
    print("Version: ", alchemy.__version__)
    print("Author: ", alchemy.__author__)


if __name__ == "__main__":
    main()
