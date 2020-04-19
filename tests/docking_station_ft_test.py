import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

def test_docking_station_release_empty():
    with pytest.raises(ValueError):
        dock.release()

def test_docking_station_release():
    bike1 = Bike("newBike") 
    dock.deposit(bike1)
    assert dock.release() == bike1
    print('dock', dock)

def test_docking_station_deposit():
    bike2 = Bike("dockingBike")
    assert dock.deposit(bike2) == [bike2]

def test_docking_station_max_cap():
    del dock.rack[:]
    for i in range(1,21):
        i = dock.deposit(Bike('1'))
    bike11 = Bike('bike11')
    with pytest.raises(ValueError):
        dock.deposit(bike11)

def test_bikes_available():
    del dock.rack[:]
    bike3 = Bike("availableBike")
    dock.deposit(bike3)
    assert dock.available() == [bike3]
