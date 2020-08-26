from classes import *

class AirPlaneFactory(Factory):
  def __init__(self, hp, base_cost, zone):
    super().__init__(hp, base_cost)
class AntiAircraftFactory(Factory):
  def __init__(self, hp, base_cost, zone):
    super().__init__(hp, base_cost)
class ArmamentFactory(Factory):
  def __init__(self, hp, base_cost, zone):
    super().__init__(hp, base_cost)


def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
