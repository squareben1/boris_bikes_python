import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

def test_docking_station_release():
    bike = "newBike"
    dock.deposit(bike)
    assert dock.release() == bike

def test_docking_station_deposit():
    bike = "dockingBike"
    dock.deposit(bike)
    assert dock.rack == [bike]

def test_bikes_available():
    dock.release()
    bike3 = "availableBike"
    dock.deposit(bike3)
    assert dock.available() == [bike3]

def test_docking_station_max_cap():
    del dock.rack[:]
    dock.rack = list(range(1,21))
    bike11 = 'bike11'
    with pytest.raises(ValueError):
        dock.deposit(bike11)