from bike import Bike

class DockingStation:

    def __init__(self, location):
        self.location = location

    def release(self):
        return Bike("BMX")