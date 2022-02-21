class Building:
    year = None
    city = None

    def __init__(self, year, city):
        self.year = year
        self.city = city

    def get_info(self):
        print("Year: ", self.year, ".", "City: ", self.city)


class School(Building):
    pupils = None

    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city)
        self.pupils = pupils


class House(Building):
    pass


class Shop(Building):
    pass


school = School(10, 1995, "New York")
house = House(2000, "Moscow")
shop = Shop(2001, "Kyiv")


school.get_info()
