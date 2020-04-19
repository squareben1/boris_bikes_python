import pytest
from lib import DockingStation
from lib import Bike
from doubles import InstanceDouble, allow

dock = DockingStation('London')

class BikeDouble:
    def __init__(self,model):
        self.model = model
        self.working = True

    def report_broken(self):
        self.working = False
        return self.working

@pytest.fixture(autouse=True)
def clear_rack():
    del dock.rack[:]

bike = BikeDouble("newBike")
bike2 = BikeDouble("secondBike")

def test_docking_station_release():
    dock.deposit(bike)
    assert dock.release() == bike

def test_docking_station_deposit():
    dock.deposit(bike)
    assert dock.rack == [bike]

def test_bikes_available():
    dock.deposit(bike)
    assert dock.available() == [bike]

def test_docking_station_max_cap():
    dock.rack = list(range(1,21))
    with pytest.raises(ValueError):
        dock.deposit(bike)

def test_user_set_max():
    dock2 = DockingStation('Brighton', 1)
    dock2.rack.append(bike)
    with pytest.raises(ValueError):
        dock2.deposit(bike2)

# Note: fix this test when python version problems resolved, use double
def test_report_broken():
    broken_bike = BikeDouble('busted')
    print('broken_bike', broken_bike)
    assert dock.deposit(broken_bike, True)[0].working == False
    
def test_release_broken_bike():
    dock.deposit(bike, True)
    with pytest.raises(ValueError):
        dock.release()

def test_release_working_bike_only():
    bike.working = True
    dock.deposit(bike)
    dock.deposit(bike2, True) # deposit broken bike
    assert dock.release() == bike #expect to release the working bike
