
class Cat:
    name = None
    age = None
    isHappy = None

    def set_data(self, name, age, isHappy):  #self - должно быть так как мы сделали функцию в классе
        self.name = name
        self.age = age
        self.isHappy = isHappy

    def get_data(self):
        print(self.name, self.age, self.isHappy)

cat1 = Cat()
cat1.set_data("Bars", 3, True)
# cat1.name = "Bars"
# cat1.age = 3
# cat1.isHappy = True

cat2 = Cat()
cat2.set_data("Mars", 2, None)
# cat2.name = "Mars"
# cat2.age = 2
# cat2.isHappy = None

# print(cat1.name)
# print(cat2.isHappy)

cat1.get_data()
cat2.get_data()

