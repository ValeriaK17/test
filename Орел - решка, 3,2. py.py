# Орел \ Решка
# Глава 3. Задание 2

print ("Программа 100 раз подбросит монету и подсчитает сколько раз выподет 'орел' и 'решка'.")

orel = int(0)
reshka = int(0)
all_podbros = int (0)
import random
podbros = int(0)
while all_podbros != 100:
    podbros = random.randint (1, 2)
    if podbros == 1:
        orel +=1
        all_podbros +=1
    if podbros == 2:
        reshka +=1
        all_podbros +=1
    

    
print ("\nВыпало орлов:", orel,)
print ("\nВыпало решек:", reshka)

input ("\nНажмите Enter, чтобы выйти ")
