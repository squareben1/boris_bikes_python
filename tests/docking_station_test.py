import pytest
from lib import DockingStation

dock = DockingStation('London')

def test_docking_station_release():
    assert dock.release() == "Bike"
