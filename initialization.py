from classes import *


class AirCraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "AirCraftFactory")
        self.zone = zone


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
    temp_factory = AirCraftFactory(forest_zone)
    p1.addFactory(temp_factory)
    temp_factory = AirCraftFactory(mountain_zone)
    p1.addFactory(temp_factory)
    print(p1.factories[0].zone.name)

if __name__ == "__main__":
    main()
