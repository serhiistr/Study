import openpyxl

wb = openpyxl.reader.excel.load_workbook(filename="basestudent.xlsx")

# print(wb.sheetnames)
wb.active = 0
sheet = wb.active
# print(sheet['A1'].value)

for i in sheet:
    print(sheet['A1'+str(i)].value, sheet['B1'+str(i)].value, sheet['C'+str(i)].value)