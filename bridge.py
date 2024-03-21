class Bridge:
    def __init__(self):
        self.vehicles = []
        self.max_vehicles = 20
        self.max_weight = 30000

    def calc_weight(self):
        total_weight = 0
        for vehicle in self.vehicles:
            total_weight += vehicle.weight

        return total_weight

    def add_vehicle(self, vehicle):
        if (self.calc_weight() + vehicle.weight) > self.max_weight:
            return
        elif len(self.vehicles) + 1 > self.max_vehicles:
            return

        self.vehicles.append(vehicle)

    def remove_vehicle(self, reg_num):
        for vehicle in self.vehicles:
            if vehicle.reg_num == reg_num:
                self.vehicles.remove(vehicle)
                break
