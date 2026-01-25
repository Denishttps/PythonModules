
class SecurePlant:
    def __init__(self, name, height, age):
        self.name: str = name
        self._height: int
        self._age: int

        self._on_create()
        self.set_height(height)
        self.set_age(age)

    def _on_create(self):
        print("Plant created:", self.name)

    def set_height(self, height):
        if height < 0:
            print(
                f"Invalid operation attempted: height {height}cm [REJECTED]\n"
                "Security: Negative height rejected"
            )
            return
        self._height = height
        print(f"Height updated: {height}cm [OK]")

    def set_age(self, age):
        if age < 0:
            print(
                f"Invalid operation attempted: age {age} days [REJECTED]\n"
                "Security: Negative age rejected"
            )
            return
        self._age = age
        print(f"Age updated: {age} days [OK]")

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

    def get_info(self):
        print(
            f"Current Plant: "
            f"{self.name} ({self.get_height()}cm, {self.get_age()} days)"
        )


def main():
    print("=== Garden Security System ===")
    plant = SecurePlant("Rose", 25, 45)
    print('')
    plant.set_height(-5)
    print('')
    plant.get_info()


if __name__ == "__main__":
    main()
