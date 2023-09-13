# Определение структуры student
class Student:
    def __init__(self, name, surname, number, facult):
        self.name = name
        self.surname = surname
        self.number = number
        self.facult = facult
        
# Функция для поиска студента по заданным параметрам
def search_student(students, name, surname, number, facult):
    for student in students:
        if student.name == name and student.surname == surname and student.number == number and student.facult == facult:
            return student
    return None

# Создание списка студентов
students = [
    Student("Иван", "Иванов", 1, "ФВТ"),
    Student("Петр", "Петров", 2, "ФИТЭ"),
    Student("Сергей", "Сидоров", 3, "ФППиСН"),
    Student("Алексей", "Алексеев", 4, "ИФФ"),
]

# Ввод параметров для поиска
search_name = input("Введите имя студента: ")
search_surname = input("Введите фамилию студента: ")
search_number = int(input("Введите номер зачётной книжки студента: "))
search_facult = input("Введите факультет студента: ")

# Поиск студента по заданным параметрам
found_student = search_student(students, search_name, search_surname, search_number, search_facult)

# Проверка результатов поиска
if found_student is None:
    print("Студент не найден")
else:
    print("Студент найден:")
    print("Имя:", found_student.name)
    print("Фамилия:", found_student.surname)
    print("Номер зачётной книжки:", found_student.number)
    print("Факультет:", found_student.facult)
