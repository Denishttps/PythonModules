
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def _get_info(self):
        return (
            f"{self.name} ({self.__class__.__name__}): "
            f"{self.height}cm, {self.age} days"
        )

    def get_info(self):
        raise NotImplementedError("Subclasses must implement get_info method")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color

    def bloom(self):
        return f"{self.name} is blooming beautifully!"

    def get_info(self):
        print(
            self._get_info() + f", {self.color} color",
            self.bloom(),
            sep='\n'
        )


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter):
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        return (
            f"{self.name} provides {self.trunk_diameter * 10} "
            "square meters of shade"
        )

    def get_info(self):
        print(
            self._get_info() + f", {self.trunk_diameter}cm diameter",
            self.produce_shade(),
            sep='\n'
        )


class Vegetable(Plant):
    def __init__(
        self,
        name,
        height,
        age,
        harvest_season,
        nutritional_value
    ):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        print(
            self._get_info() +
            f", {self.harvest_season} harvest",
            self.nutritional_value,
            sep='\n'
        )


def main():
    print("=== Garden Plant Types ===")
    plants: list[list[Plant]] = [
        [
            Flower("Rose", 25, 30, "Red"),
            Flower("Tulip", 20, 25, "Yellow")
        ],
        [
            Tree("Oak", 200, 365, 50),
            Tree("Poplar", 150, 200, 30)
        ],
        [
            Vegetable(
                "Carrot",
                15,
                90,
                "Autumn",
                "Carrot is rich in Vitamin A"
            ),
            Vegetable(
                "Potato",
                20,
                120,
                "Summer",
                "Potato is rich in carbohydrates"
            )
        ]
    ]

    for i in range(len(plants)):
        for plant in plants[i]:
            print('')
            plant.get_info()
        print('=' * 50)


if __name__ == "__main__":
    main()
