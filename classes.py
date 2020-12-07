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
    def __init__(self, name, materials, production_time):
        self.name = name
        self.materials = materials
        self.production_time = production_time


class Player:
    def __init__(self, player_id, posx, posy, starting_resources):
        self.player_id = player_id
        self.posx = posx
        self.posy = posy
        self.resources = starting_resources
        self.is_working = False
        self.factories = list()
        self.inventory = {"UAV": 0,
                          "Bomber": 0}

    def buildFactory(self, input_factory):
        self.is_working = True
        self.factories.append(input_factory)
        input_factory_cost = multiplyLists(input_factory.base_cost, input_factory.zone.cost_ratio)
        self.resources = subtractDicts(self.resources, input_factory_cost)
        self.is_working = False

    def addToInventory(self, product):
        self.inventory[product.name] += 1

    def produce(self, factory, product):
        self.is_working = True
        self.resources = subtractDicts(self.resources, product.materials)
        time.sleep(product.production_time)
        self.addToInventory(product)
        self.is_working = False

def main():
    print("Hello World!")


if __name__ == "__main__":
    main()
