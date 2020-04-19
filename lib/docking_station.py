from bike import Bike

class DockingStation:

    def __init__(self, location):
        self.location = location
        self.rack = []
        self.max_capacity = 10


    def deposit(self, bike):
        if len(self.rack) >= self.max_capacity:
            raise ValueError('Rack is full')
        else:
            self.rack.append(bike)
            return self.rack

    def release(self):
        if len(self.rack) > 0:
            return self.rack.pop()
        else:
            raise ValueError('Rack is empty')

    def available(self):
        return self.rack

