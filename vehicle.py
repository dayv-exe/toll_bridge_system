from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, reg_num, weight):
        reg_num = self.reg_num
        weight = self.weight

    @abstractmethod
    def calculate_fee(self):
        pass
