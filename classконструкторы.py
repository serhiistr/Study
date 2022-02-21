
class Cat:
    name = None
    age = None
    isHappy = None

    def __init__(self, name, age, isHappy): #Если мы пишем два подчеркивания то мы созадем как раз конструктор
        self.name = name
        self.age = age
        self.isHappy = isHappy

        self.get_data()

    # def set_data(self, name, age, isHappy):  #self - должно быть так как мы сделали функцию в классе
    #     self.name = name
    #     self.age = age
    #     self.isHappy = isHappy

    def get_data(self):
        print(self.name, self.age, self.isHappy)

cat1 = Cat("Bars", 3, True)
cat2 = Cat("Mars", 2, None)


