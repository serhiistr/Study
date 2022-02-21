# Концепция инкапсуляции - это доступ к полям year and city напрямую
# запрещен. Досиуп возможен только через различніе функции или же конструкторы


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

    def get_info(self):
        super(School, self).get_info()
        print("Pupils: = ", self.pupils )


class House(Building):
    pass


class Shop(Building):
    pass


school = School(10, 1995, "New York")
school.get_info()
house = House(2000, "Moscow")
shop = Shop(2001, "Kyiv")

shop.get_info()

