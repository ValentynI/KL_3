class Plane:
    def __init__(self, fuel, flight_range):
        self.fuel = fuel
        self.flight_range = flight_range

    def fly(self):
        if self.fuel > 0:
            print('VXZHHHHHHHH')
            self.fuel -= 1
        else:
            print('No fuel!')


class WarPlane(Plane):
    pass


f16 = WarPlane(100, 20000)
f16.fly()