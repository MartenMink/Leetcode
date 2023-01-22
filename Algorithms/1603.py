"""
task:
1603. Design Parking System
"""


class ParkingSystem:
    type_places = {}
    def __init__(self, big: int, medium: int, small: int):
        self.type_places[1] = big
        self.type_places[2] = medium
        self.type_places[3] = small

    def addCar(self, carType):
        if self.type_places[carType] > 0:
            self.type_places[carType] -= 1
            return True
        else:
            return False


obj = ParkingSystem(1, 1, 0)
param_1 = obj.addCar(3)
