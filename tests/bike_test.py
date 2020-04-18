import pytest
from lib import Bike

bike = Bike('citi')

def test_bike_working():
    assert bike.working() == True
