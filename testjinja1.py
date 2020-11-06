from jinja2 import Template

cars = [
    {'model': 'Audi', 'price': 23800},
    {'model': 'Skoda', 'price': 17500},
    {'model': 'Volvo', 'price': 45200},
    {'model': 'Volw', 'price': 22000}
    ]

tpl = "Сумма цен авто {{ (cs | max(attribute='price')).model }}"
tm = Template(tpl)
msg = tm.render(cs=cars)

print(msg)