class first_m:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def returnName(self):
        return self.name
    def returnAge(self):
        return self.age
    def __str__(self):
        return f"{self.name} ({self.age})"

person = first_m("Lalith", 4)
print(person)
