import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

# def test_docking_station_release():
#     bike = dock.release()
#     assert bike.working() == True

def test_docking_station_deposit():
    bike = "dockingBike"
    dock.deposit(bike)
    assert dock.rack == [bike]