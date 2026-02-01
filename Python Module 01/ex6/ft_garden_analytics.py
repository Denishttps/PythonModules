
class Plant:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
        self.growth = 0

    def grow(self):
        self.height += 1
        self.growth += 1
        print(f"{self.name} grew 1cm")

    def get_type(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, color: str):
        super().__init__(name, height)
        self.color = color
        self.is_blooming = False

    def bloom(self):
        self.is_blooming = True

    def get_type(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, color: str, prize_points: int):
        super().__init__(name, height, color)
        self.prize_points = prize_points

    def get_type(self):
        return "prize"


class Garden:
    def __init__(self, owner: str):
        self.owner = owner
        self.plants = []

    def add_plant(self, plant: Plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.owner}'s garden")

    def grow_all(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()

    def get_plants(self):
        return self.plants


class GardenManager:
    gardens = []

    class GardenStats:
        @staticmethod
        def total_growth(plants):
            total = 0
            for plant in plants:
                total += plant.growth
            return total

        @staticmethod
        def count_types(plants):
            regular = 0
            flowering = 0
            prize = 0

            for plant in plants:
                t = plant.get_type()
                if t == "regular":
                    regular += 1
                elif t == "flowering":
                    flowering += 1
                elif t == "prize":
                    prize += 1
            return regular, flowering, prize

    def __init__(self):
        pass

    def add_garden(self, garden: Garden):
        self.gardens.append(garden)

    @classmethod
    def create_garden_network(cls):
        scores = {}
        for garden in cls.gardens:
            score = 0
            for plant in garden.get_plants():
                score += plant.height
                if plant.get_type() == "prize":
                    score += plant.prize_points
            scores[garden.owner] = score
        return scores

    @staticmethod
    def validate_height(height):
        return height > 0


def main():
    print("=== Garden Management System Demo ===")

    manager = GardenManager()

    alice = Garden("Alice")
    bob = Garden("Bob")

    manager.add_garden(alice)
    manager.add_garden(bob)

    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    rose.bloom()
    sunflower.bloom()

    alice.add_plant(oak)
    alice.add_plant(rose)
    alice.add_plant(sunflower)

    alice.grow_all()

    print("=== Alice's Garden Report ===")
    print("Plants in garden:")
    for plant in alice.get_plants():
        if plant.get_type() == "regular":
            print(f"- {plant.name}: {plant.height}cm")
        elif plant.get_type() == "flowering":
            print(
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming)"
            )
        else:
            print(
                f"- {plant.name}: {plant.height}cm, "
                f"{plant.color} flowers (blooming), "
                f"Prize points: {plant.prize_points}"
            )

    stats = GardenManager.GardenStats
    total_growth = stats.total_growth(alice.get_plants())
    r, f, p = stats.count_types(alice.get_plants())

    print(
        f"Plants added: {len(alice.get_plants())}, "
        f"Total growth: {total_growth}cm"
    )
    print(f"Plant types: {r} regular, {f} flowering, {p} prize flowers")

    print(f"Height validation test: {GardenManager.validate_height(10)}")

    scores = GardenManager.create_garden_network()
    print(
        f"Garden scores - Alice: {scores['Alice']}, "
        f"Bob: {scores.get('Bob', 0)}"
    )
    print(f"Total gardens managed: {len(GardenManager.gardens)}")


if __name__ == "__main__":
    main()
