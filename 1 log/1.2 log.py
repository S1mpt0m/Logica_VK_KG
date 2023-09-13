import random

# Создание пустого массива
mass = []
counter = 0

# Заполнение массива 10 случайными числами от 0 до 100
while counter != 10:
    mass.append(random.randint(0,100))
    counter += 1
    
# Вывод массива
print(mass)
