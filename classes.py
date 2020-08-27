from miscellaneousFunctions import *


class Factory:
    def __init__(self, hp, base_cost, name):
        self.hp = hp
        self.base_cost = base_cost
        self.zone = None
        self.name = name


class Zone:
    def __init__(self, risk, cost_ratio, name):
        self.risk = risk
        self.cost_ratio = cost_ratio
        self.name = name


class Player:
    def __init__(self, player_id, posx, posy, starting_resources):
        self.player_id = player_id
        self.posx = posx
        self.posy = posy
        self.resources = starting_resources
        self.factories = list()

    def addFactory(self, input_factory):
        self.factories.append(input_factory)
        input_factory_cost = multiplyLists(input_factory.base_cost, input_factory.zone.cost_ratio)
        self.resources = subtractLists(self.resources, input_factory_cost)


def main():
    print("Hello World!")


if __name__ == "__main__":
    main()