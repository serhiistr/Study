from jinja2 import Template

# name = "Федор"
# age = 28
#
# tm = Template("Мне {{ a*2 }} лет и зовут {{ n.upper() }}")
# msq = tm.render(a=age, n=name)
#
# print(msq)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def getName(self):
#         return self.name
#
#     def getAge(self):
#         return self.age
#
# per = Person("Ivan", 28)
#
# tm = Template("Мне {{ p.getName() }} лет и зовут {{ p.getAge() }}")
# msq = tm.render(p=per)
#
# print(msq)

data = '''{% raw%}Модуль Jinja вместо
определения {{ name }}
подставляет соответсвующее значение{% endraw%}'''

tm = Template(data)
msq = tm.render(name='Ivan')

print(msq)