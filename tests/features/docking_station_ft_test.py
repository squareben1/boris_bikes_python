import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

@pytest.fixture(autouse=True)
def clear_rack():
    del dock.rack[:]

bike = Bike("newBike")
bike2 = Bike("otherBike")

def test_docking_station_release_empty():
    with pytest.raises(ValueError):
        dock.release()

def test_docking_station_release():
    dock.deposit(bike)
    assert dock.release() == bike
    print('dock', dock)

def test_docking_station_deposit():
    assert dock.deposit(bike) == [bike]

def test_docking_station_max_cap():
    for i in range(1,21):
        i = dock.deposit(Bike('1'))
    with pytest.raises(ValueError):
        dock.deposit(bike)

def test_bikes_available():
    dock.deposit(bike)
    assert dock.available() == [bike]

def test_user_set_maximum():
    dock2 = DockingStation('Brighton',1)
    dock2.deposit(bike)
    with pytest.raises(ValueError):
        dock2.deposit(bike2)

def test_report_broken():
    dock.deposit(bike, True)
    assert dock.rack[0].working == False
    
def test_release_broken_bike():
    dock.deposit(bike, True)
    with pytest.raises(ValueError):
        dock.release()

def test_release_working_bike_only():
    bike.working = True
    dock.deposit(bike)
    dock.deposit(bike2, True) # deposit broken bike
    assert dock.release() == bike #expect to release the working bike
