import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

@pytest.fixture(autouse=True)
def run_around_tests():
    files_before = clear_rack()

def clear_rack():
    del dock.rack[:]

def test_docking_station_release():
    bike = "newBike"
    dock.deposit(bike)
    assert dock.release() == bike

def test_docking_station_deposit():
    bike = "dockingBike"
    dock.deposit(bike)
    assert dock.rack == [bike]

def test_bikes_available():
    bike3 = "availableBike"
    dock.deposit(bike3)
    assert dock.available() == [bike3]

def test_docking_station_max_cap():
    dock.rack = list(range(1,21))
    bike11 = 'bike11'
    with pytest.raises(ValueError):
        dock.deposit(bike11)

def test_user_set_max():
    dock2 = DockingStation('Brighton', 1)
    dock2.rack.append('bikeA')
    with pytest.raises(ValueError):
        dock2.deposit('bikeB')
    