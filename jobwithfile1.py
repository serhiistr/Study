# data_1 = input("Введите текст: ")
#
# file = open("Data/text_1.txt", "w")
#
# file.write(data_1+"\n")
#
# file.close()

#
# #учимся считывать информацию
#
# file_1 = open("Data/text_1.txt", "r")
#
# #print(file_1.read())
# print(file_1.read(1)) #выводит количество символов
#
# file_1.close()


# учимся считывать информацию построчно

file_1 = open("Data/text_1.txt", "r")

for line in file_1:
    print(line, end="")

file_1.close()
