# Глава 4. Задание 1

nachalo = int (input ("Введите число, которое является началом отсчета "))
konec = int (input ("Введите число, которое является концом счета "))
interval = int( input ("Введите число, равное значению интервала "))

for i in range (nachalo, konec, interval):
    print (i, end = " ")

input ("\nНажмите Enter, чтобы выйти")
