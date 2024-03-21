from vehicle import Vehicle


class Lorry(Vehicle):
    def __init__(self, reg_num, weight):
        self.reg_num = reg_num
        self.weight = weight

    def calculate_fee(self):
        lorry_fee = 10.00 if self.weight  <= 8000 else 15.00

        return lorry_fee
