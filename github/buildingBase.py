class Building:
    def __init__(self, south, west, width_WE, width_NS, height=10):
        self.south = south
        self.west = west
        self.width_WE = width_WE
        self.width_NS = width_NS
        self.height = height

    def corners(self):
        dict = {}
        dict["north-west"] = [self.south + self.width_NS, self.west]
        dict["north-east"] = [self.south + self.width_NS, self.west + self.width_WE]
        dict["south-west"] = [self.south, self.west]
        dict["south-east"] = [self.south, self.west + self.width_WE]
        return dict

    def area(self):
        return self.width_WE * self.width_NS

    def volume(self):
        return self.area() * self.height

    def __repr__(self):
        return ("Building("+str(self.south)+", " + str(self.west) + ", "
        + str(self.width_WE) + ", " + str(self.width_NS) + ", " + str(self.height) + ")")
