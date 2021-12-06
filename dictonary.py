# country = {4: 3}
# print(country[4])
#
# country = {True: 3}
# print(country[True])
#
# country = {"tr": 3}
# print(country["tr"])
#
# country = {(5, 6): 4}
# print(country[(5, 6)])
#
#
# country = {"code": "RU", "name": "Russia", "population": 144}
# print(country["name"])
#
# country = dict(code="RU", name="Rissia")
# print(country["code"])

# country = {"code": "RU", "name": "Russia", "population": 144}
# for key, value in country.items():
#     print(key, " - ", value)

# country = {"code": "RU", "name": "Russia", "population": 144}
# print(country.get("name"))
#
# country = {"code": "RU", "name": "Russia", "population": 144}
# print(country.clear())
#
# country = {"code": "RU", "name": "Russia", "population": 144}
# country.pop("name")
# print(country)
#
# country = {"code": "RU", "name": "Russia", "population": 144}
# country.popitem()
# print(country)
#
# country = {"code": "RU", "name": "Russia", "population": 144}
# print(country.keys())
# print(country.values())
#
# country["code"] = "None"
# print(country.items())

person = {
    "user_1": {
        "First_name": "John",
        "Last_name": "Marley",
        "age": 45,
        "address": ("C.Kyiv", "street Khreshchatyk", "house", 45),
        "grades": {"math":5, "physics": 3}
    },
    "user_2": {

    }
}

print(person["user_1"]["address"][1])
print(person["user_1"]["address"])
print(person["user_1"])
