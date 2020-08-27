from classes import *


class AirPlaneFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100})
        self.zone = zone


class AntiAircraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100})
        self.zone = zone


class ArmamentFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100})
        self.zone = zone


forest_zone = Zone(0.5, [1, 1, 1])
plain_zone = Zone(0.7, [2, 1, 3])
mountain_zone = Zone(0.1, [3, 5, 4])


def main():
    starting_resources = {"Fuel": 1000, "Money": 1000, "Iron": 1000}
    p1 = Player("810977144", 0, 0, starting_resources)
    temp_factory = AirPlaneFactory(forest_zone)
    p1.addFactory(temp_factory)
    temp_factory = AirPlaneFactory(mountain_zone)
    p1.addFactory(temp_factory)
    print(p1.factories[0].zone)

if __name__ == "__main__":
    main()
