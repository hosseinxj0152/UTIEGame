from classes import *


class AirCraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "AirCraftFactory")
        self.zone = zone

    UAV = Product("UAV", {"Fuel": 10, "Money": 10, "Iron": 10}, 3)
    Bomber = Product("Bomber", {"Fuel": 15, "Money": 15, "Iron": 15}, 5)


class AntiAircraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "AntiAirCraftFactory")
        self.zone = zone


class ArmamentFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "ArmamentFactory")
        self.zone = zone


forest_zone = Zone(0.5, {"Fuel": 1, "Money": 1, "Iron": 1}, "forest_zone")
plain_zone = Zone(0.7, {"Fuel": 1, "Money": 1, "Iron": 1}, "plain_zone")
mountain_zone = Zone(0.1, {"Fuel": 1, "Money": 1, "Iron": 1}, "mountain_zone")


def main():
    starting_resources = {"Fuel": 1000, "Money": 1000, "Iron": 1000}
    p1 = Player("810977144", 0, 0, starting_resources)
    temp_factory = AirCraftFactory(plain_zone)
    p1.addFactory(temp_factory)
    temp_factory = AirCraftFactory(mountain_zone)
    p1.addFactory(temp_factory)
    p1.produce(temp_factory,temp_factory.UAV)
    print(p1.inventory)


if __name__ == "__main__":
    main()
