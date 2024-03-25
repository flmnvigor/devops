import math

print("Квадратное уравнение.")
bad_data = True
while bad_data == True:
    try:
        a = int(input("Введите a: "))
        b = int(input("Введите b: "))
        c = int(input("Введите c: "))
        bad_data = False
    except ValueError:
        print("value error")

D = b*b - (4*a*c)
print(D)
