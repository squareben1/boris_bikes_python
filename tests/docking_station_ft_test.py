import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

def test_docking_station_release():
    bike = dock.release()
    assert bike.working() == True

def test_docking_station_deposit():
    bike = Bike("dockingBike")
    assert dock.deposit(bike) == [bike]