class Universe:
    def __init__(self, planets, howBig):
        self.planets = planets
        self.howBig = howBig
    def getPlanets(self):
        print("There are " + str(self.planets) + " planets in the universe.")
class Earth(Universe):
    def __init__(self, planets, howBig):
        self.planets=planets
        self.howBig = howBig
    def getPlanets(self):
        print("Earth is just a planet")
x1 = Universe(490, 300)
y1 = Earth(1, 304)
x1.getPlanets()
y1.getPlanets()
