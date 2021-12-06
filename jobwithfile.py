file = open("Data/text.txt", "w") #write - обновляет информацию в файле text.txt стирая старую.

file.write("Hello")  #сделали запись в файл
file.write("!!!\n")

file.write("Hello")
file.write("!!!")


#псоле открытия файла надо его сразу закрыть, иначе будет утечка памяти!!!
file.close()


file = open("Data/text.txt", "a") #append - добавляет новую информацию в файл text.txt

file.write("Serhii")

#псоле открытия файла надо его сразу закрыть, иначе будет утечка памяти!!!
file.close()
