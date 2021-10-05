import random
 
print("\tДобро пожаловать в игру 'Отгадай число'!")
print("Компьютер загадал натуральное число из диапазона от 1 до 100.")
print("Вам нужно угадать его за максимум 5 попыток.\n")
 
# Начальные значения
the_number = random.randint(1, 100)
guess = int(input("Ваше предположение: "))
tries = 0
 
# Цикл отгадывания
while guess!= the_number:
    if guess > the_number:
        print("Меньше...")
        tries +=1
    elif guess < the_number:
        print("Больше...")
        tries +=1
    if guess > the_number and tries >= 5:
        print("Ну же!")
        break
    elif guess < the_number and tries >= 5:
        print("Неудачник!")
        break
    guess = int(input("Ваше предположение: "))
   
if guess == the_number:
    print("\nПоздравляю! Вам удалось отгадать число!")
    print("вы затратили всего лишь", tries, "попытки(ок)!")
else:
    print ("\nТы лох")

input("\nНажмите Enter, чтобы покинуть игру...")
