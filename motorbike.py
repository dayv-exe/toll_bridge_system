from vehicle import Vehicle


class Motorbike(Vehicle):
    def __init__(self, reg_num, weight):
        self.reg_num = reg_num
        self.weight = weight

    def calculate_fee(self):
        motorbike_fee = 3.00
        return motorbike_fee
