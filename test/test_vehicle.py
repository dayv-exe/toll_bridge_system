import pytest
from lorry import Lorry
from motorbike import Motorbike
from car import Car


def test_small_lorry():
    lorry = Lorry("32", 5000)
    assert lorry.calculate_fee() == 10


def test_motorbike():
    bike = Motorbike("abc", 400)
    assert bike.calculate_fee() == 3


def test_car():
    car1 = Car("abc", 1590)
    assert car1.calculate_fee() == 5
    car2 = Car("abc", 1690)
    assert car2.calculate_fee() == 5.10


