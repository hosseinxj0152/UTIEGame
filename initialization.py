from classes import *

Caliber_35 = armament(name="Caliber_35",
                      materials={"Fuel": 0.002, "Money": 0.002, "Iron": 0.002},
                      production_time=3,
                      damage=0.1)
Caliber_20 = armament(name="Caliber_20",
                      materials={"Fuel": 0.002, "Money": 0.002, "Iron": 0.002},
                      production_time=0.00001,
                      damage=.07)
Reconnaissance_aircraft = aircraft(name="Reconnaissance_aircraft",
                                   materials={"Fuel": 10, "Money": 10, "Iron": 10},
                                   production_time=3)
B_2_Spirit = aircraft(name="B_2_Spirit",
                      materials={"Fuel": 15, "Money": 15, "Iron": 15},
                      production_time=4,
                      caliber=Caliber_35, capacity=5)
Marksman = antiaircraft(name="Marksman",
                        materials={"Fuel": 5, "Money": 5, "Iron": 5},
                        production_time=2,
                        caliber=Caliber_35,
                        capacity=10)
Macbeth = antiaircraft(name="Macbeth",
                       materials={"Fuel": 4, "Money": 4, "Iron": 4},
                       production_time=1,
                       caliber=Caliber_20,
                       capacity=15)
forest_zone = Zone(0.5, {"Fuel": 1, "Money": 1, "Iron": 1}, "forest_zone")
plain_zone = Zone(0.7, {"Fuel": 1, "Money": 1, "Iron": 1}, "plain_zone")
mountain_zone = Zone(0.1, {"Fuel": 1, "Money": 1, "Iron": 1}, "mountain_zone")


def main():
    starting_resources = {"Fuel": 1000, "Money": 1000, "Iron": 1000}
    p1 = Player("810977144", 0, 0, starting_resources)
    temp_factory = ArmamentFactory(plain_zone)
    p1.buildFactory(temp_factory)
    p1.produce(temp_factory, Caliber_35)
    print(p1.inventory)
    print(p1.resources)
    print(p1.factories)


if __name__ == "__main__":
    main()
