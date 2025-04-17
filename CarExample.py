class Car:
    def __init__(self, model, brand, allWheelDrive):
        self.carModel = model
        self.carBrand = brand
        self.canCarDrive4W = allWheelDrive
    def __str__(self):
        return f"{self.carModel} {self.carBrand} {self.canCarDrive4W}"
    def returnBrand(self):
        return(self.carBrand)
class Toyota(Car):
    carModel = "RAV 4"
    brand = "Toyota"
    allWheelDrive = True
    def __init__(self, yearsDriven):
        super().__init__(self.carModel, self.brand, self.allWheelDrive)
        self.yearsDriven = yearsDriven
toyotaCar = Toyota(4)
print(toyotaCar)
print(toyotaCar.returnBrand())
