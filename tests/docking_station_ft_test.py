import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

def test_docking_station_release_empty():
    assert dock.release() == "Rack is empty"

def test_docking_station_release():
    bike1 = Bike("newBike") 
    dock.deposit(bike1)
    assert dock.release() == bike1

def test_docking_station_deposit():
    bike2 = Bike("dockingBike")
    assert dock.deposit(bike2) == [bike2]

def test_bikes_available():
    dock.release()
    bike3 = Bike("availableBike")
    dock.deposit(bike3)
    assert dock.available() == [bike3]