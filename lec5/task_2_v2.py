# Вводятся три разных числа. Найти, какое из них является средним
# (Больше одного, но меньше другого)
print ("Введите три разных числа")
number_1 = float (input ("Введите первое число: "))
number_2 = float (input ("Введите второе число: "))
number_3 = float (input ("Введите третье число: "))
# проверяем, все ли числа разные
if (number_1 == number_2 or number_1 == number_3 or number_2 == number_3):
    print ("Вы ввели несколько одинаковых чисел.")
    print ("Но числа должны быть разными.")
    print ("Попробуйте еще раз.")
else:
    # сортировка по возрастанию
    # выводим числа в начальном порядке
    print (number_1, " ", number_2, " ", number_3)
    # выбираем наибольшее число из всех трех
    if number_1 > number_2:
        temp = number_2
        number_2 = number_1
        number_1 = temp
    # выводим результаты сортировки
    print (number_1, " ", number_2, " ", number_3)
    if number_2 > number_3:
        temp = number_3
        number_3 = number_2
        number_2 = temp
    # выводим результаты сортировки
    print (number_1, " ", number_2, " ", number_3)
    # выбираем наибольшее число из оставшихся первых двух
    if number_1 > number_2:
        temp = number_2
        number_2 = number_1
        number_1 = temp
    # выводим результаты сортировки
    print (number_1, " ", number_2, " ", number_3)
    # в отсортированной последовательности 2-е число среднее
    print ("Среднее число ", number_2)
