from bike import Bike

class DockingStation:

    def __init__(self, location, max_capacity=20):
        self.location = location
        self.rack = []
        self.__max_capacity = max_capacity

    def set_broken_bike(self, bike):
        bike.report_broken()
        return bike

    def deposit(self, bike, broken=False):
        if self.__rack_full():
            raise ValueError('Rack is full')
        elif broken == True:
            self.rack.append(self.set_broken_bike(bike))
            return self.rack
        else:
            self.rack.append(bike)
            return self.rack      

    def release(self):
        working_bikes = 0
        for i in range(len(self.rack)):
            if self.rack[i].working:
                working_bikes += 1

        if not self.__rack_empty():
            if working_bikes > 0:
                for i in range(len(self.rack)):
                    if self.rack[i].working:
                        return self.rack.pop(i)
            else: 
                raise ValueError('No Working Bikes')
        else:
            raise ValueError('Rack is empty')

    def available(self):
        return self.rack

    def __rack_full(self):
        if len(self.rack) >= self.__max_capacity:
            return True
        else:
            return False
    def __rack_empty(self):
        if len(self.rack) > 0:
            return False
        else:
            return True
