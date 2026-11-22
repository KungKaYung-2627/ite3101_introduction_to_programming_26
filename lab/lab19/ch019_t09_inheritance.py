class Car(object):

    def __init__(self, model: str, color: str, mpg: int):
        self.condition = "new"
        self.model = model
        self.color = color
        self.mpg = mpg

    def display_car(self):
        return "This is a %s %s with %s MPG." % (
            self.color, self.model, self.mpg
        )

    def drive_car(self):
        self.condition = "used"


class ElectricCar(Car):
    def __init__(self, model: str, color: str, mpg: int, battery_type: str):
        super().__init__(model, color, mpg)
        self.battery_type = battery_type


my_car = ElectricCar("DeLorean", "silver", 88, "molten salt")
