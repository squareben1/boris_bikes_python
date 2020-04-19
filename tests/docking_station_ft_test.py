import pytest
from lib import DockingStation
from lib import Bike

dock = DockingStation('London')

@pytest.fixture(autouse=True)
def clear_rack():
    del dock.rack[:]

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
    for i in range(1,21):
        i = dock.deposit(Bike('1'))
    bike11 = Bike('bike11')
    with pytest.raises(ValueError):
        dock.deposit(bike11)

def test_bikes_available():
    bike3 = Bike("availableBike")
    dock.deposit(bike3)
    assert dock.available() == [bike3]

def test_user_set_maximum():
    dock2 = DockingStation('Brighton',1)
    bike4 = Bike("overDock")
    bike5 = Bike("overDock2")
    dock2.deposit(bike4)
    with pytest.raises(ValueError):
        dock2.deposit(bike5)

