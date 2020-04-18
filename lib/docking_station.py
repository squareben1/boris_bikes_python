from bike import Bike

class DockingStation:

    def __init__(self, location):
        self.location = location
        self.rack = []

    def release(self):
        return Bike("BMX")

    def deposit(self, bike):
        return self.rack.append(bike)

