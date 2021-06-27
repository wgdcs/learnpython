# Задан список строк. В каждой строке подсчитать количество вхождений заданного символа
myList = ["Race Nation", "Spartan Race", "Dyka Gonka", "Bizon Race", "Legion Run"]
myChar1 = "R"
myChar2 = "r"
for value in myList:
    print(value + ":")
    print(myChar1 + ": " + (str)(value.count(myChar1)))
    print(myChar2 + ": " + (str)(value.count(myChar2)))

