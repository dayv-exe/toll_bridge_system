import math

from vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, reg_num, weight):
        self.reg_num = reg_num
        self.weight = weight

    def calculate_fee(self):
        car_fee = 5.00
        car_max_weight = 1590
        if self.weight > car_max_weight:
            car_fee += math.floor(((self.weight - car_max_weight) / 100)) * .10

        return car_fee
