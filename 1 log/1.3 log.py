# Получание размера массива
lenm = int(input("Ведите размер массива: "))

# Создание пустого массива
mass = []
counter = 0

# Увеличение размера массива до нужного путём добавление в него пустых элементов
while counter != lenm:
    mass.append(" ")
    counter += 1

# Вывод массива
print(mass)
