import pytest
from lib import Bike

bike = Bike('citi')

def test_bike_broken():
    assert bike.report_broken() == False