# import openpyxl
#
# wb = openpyxl.reader.excel.load_workbook(filename="basestudent.xlsx")
#
# # print(wb.sheetnames)
# wb.active = 0
# sheet = wb.active
# # print(sheet['A1'].value)
#
# for i in sheet:
#     print(sheet['A1'+str(i)].value, sheet['B1'+str(i)].value, sheet['C'+str(i)].value)


import random

# city_list = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
# print("Выбор случайного города из списка - ", random.choice(city_list))


# Выборка с заменой
list = [20, 30, 40, 50, 60, 70, 80, 90]
sampling = random.choices(list, k=4)

print("Выборка с методом choices ", sampling)
