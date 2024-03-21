import pytest
from bridge import Bridge
from car import Car


def test_add_vehicle():
    dummy_car = Car('ix', 4000)

    b = Bridge()
    original_len = len(b.vehicles)
    b.add_vehicle(dummy_car)

    assert len(b.vehicles) == original_len + 1


def test_remove_vehicle():
    dummy_car = Car('ix', 4000)

    b = Bridge()
    b.add_vehicle(dummy_car)
    original_len = len(b.vehicles)

    b.remove_vehicle(dummy_car.reg_num)
    assert len(b.vehicles) == original_len - 1


def test_calc_weight():
    dummy_car = Car('ix', 6000)
    dummy_car1 = Car('v', 1000)
    dummy_car2 = Car('vi', 3000)

    b = Bridge()
    b.add_vehicle(dummy_car)
    b.add_vehicle(dummy_car1)
    b.add_vehicle(dummy_car2)

    assert b.calc_weight() == 10000


def test_bridge_weight_limit():
    dummy_car = Car('ix', 6000)
    dummy_car1 = Car('v', 1000)
    dummy_car2 = Car('vi', 3000)
    dummy_car3 = Car('vii', 5000)
    dummy_car4 = Car('viii', 13000)
    dummy_car5 = Car('ix', 7000)

    b = Bridge()
    b.add_vehicle(dummy_car)
    b.add_vehicle(dummy_car1)
    b.add_vehicle(dummy_car2)
    b.add_vehicle(dummy_car3)
    b.add_vehicle(dummy_car4)
    b.add_vehicle(dummy_car5)

    assert len(b.vehicles) == 5


def test_bridge_parking_space():
    b = Bridge()

    for i in range(22):
        small_car = Car(f"robot-{i}", 1000)
        b.add_vehicle(small_car)

    assert len(b.vehicles) == 20
