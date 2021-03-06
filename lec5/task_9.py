# Найти корни квадратного уравнения и вывести их на экран, если они есть.
# Если корней нет, то вывести сообщение об этом.
# Конкретное квадратное уравнение определяется коэффициентами a, b, c,
# которые вводит пользователь.
import math
print ("Введите коэффициенты квадратного уравнения.")
a = float (input ("Введите коэффициент a: "))
b = float (input ("Введите коэффициент b: "))
c = float (input ("Введите коэффициент c: "))
d = b * b - 4 * a * c
if d < 0:
    print ("Квадратное уравнение не имеет корней.")
elif d == 0:
    x = - b / (2 * a)
    print ("Квадратное уравнение имеет единственный корень")
    print ("x = ", x)
else:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Квадратное уравнение имеет два корня")
    print ("x1 = %s, x2 = %s" % (x1, x2))
