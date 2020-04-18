from bike import Bike

class DockingStation:

    def __init__(self, location):
        self.location = location
        self.rack = []

    def release(self):
        return self.rack.pop()

    def deposit(self, bike):
        self.rack.append(bike)
        return self.rack

