import time
from miscellaneousFunctions import *


class Factory:
    def __init__(self, hp, base_cost, name):
        self.hp = hp
        self.base_cost = base_cost
        self.zone = None
        self.name = name
        self.is_working = False


class Zone:
    def __init__(self, risk, cost_ratio, name):
        self.risk = risk
        self.cost_ratio = cost_ratio
        self.name = name


class Product:
    def __init__(self, name, materials, production_time, factory_type):
        self.name = name
        self.materials = materials
        self.production_time = production_time
        self.factory_type = factory_type


class aircraft(Product):
    def __init__(self, name, materials, production_time, caliber=None, capacity=None):
        super().__init__(name, materials, production_time,"AirCraftFactory")
        self.caliber = caliber
        self.capacity = capacity


class antiaircraft(Product):
    def __init__(self, name, materials, production_time, caliber=None, capacity=None):
        super().__init__(name, materials, production_time,"AntiAirCraftFactory")
        self.caliber = caliber
        self.capacity = capacity


class armament(Product):
    def __init__(self, name, materials, production_time, damage):
        super().__init__(name, materials, production_time,"ArmamentFactory")
        self.damage = damage


class Player:
    def __init__(self, player_id, posx, posy, starting_resources):
        self.player_id = player_id
        self.posx = posx
        self.posy = posy
        self.resources = starting_resources
        self.is_working = False
        self.is_building = False
        self.factories = {"AirCraftFactory": 0,
                          "AntiAircraftFactory": 0,
                          "ArmamentFactory": 0
                          }
        self.inventory = {"Reconnaissance_aircraft": 0,
                          "B_2_Spirit": 0,
                          "Caliber_35":0,
                          "Caliber_20":0,
                          "Marksman":0,
                          "Macbeth":0}

    def buildFactory(self, input_factory):
        self.is_building = True
        self.factories[input_factory.name] += 1
        input_factory_cost = multiplyDicts(input_factory.base_cost, input_factory.zone.cost_ratio)
        self.resources = subtractDicts(self.resources, input_factory_cost)
        self.is_building = False

    def addToInventory(self, product):
        self.inventory[product.name] += 1

    def produce(self, factory, product):
        if(factory.name == product.factory_type):
            self.is_working = True
            self.resources = subtractDicts(self.resources, product.materials)
            time.sleep(product.production_time)
            self.addToInventory(product)
            self.is_working = False


class AirCraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "AirCraftFactory")
        self.zone = zone
        self.name = "AirCraftFactory"


class AntiAircraftFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "AntiAirCraftFactory")
        self.zone = zone
        self.name = "AntiAirCraftFactory"


class ArmamentFactory(Factory):
    def __init__(self, zone):
        super().__init__(100, {"Fuel": 100, "Money": 100, "Iron": 100}, "ArmamentFactory")
        self.zone = zone
        self.name = "ArmamentFactory"


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
