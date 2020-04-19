from bike import Bike

class DockingStation:

    def __init__(self, location):
        self.location = location
        self.rack = []
        self.max_capacity = 20

    def rack_full(self):
        if len(self.rack) >= self.max_capacity:
            return True
        else:
            return False
    def rack_empty(self):
        if len(self.rack) > 0:
            return False
        else:
            return True

    def deposit(self, bike):
        if self.rack_full():
            raise ValueError('Rack is full')
        else:
            self.rack.append(bike)
            return self.rack

    def release(self):
        if not self.rack_empty():
            return self.rack.pop()
        else:
            raise ValueError('Rack is empty')

    def available(self):
        return self.rack

