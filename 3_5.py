class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def change_name(self, new_name):
        self.name = new_name

class Student(Person):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return "Список оцінок порожній"
        return sum(self.grades) / len(self.grades)

# створення студента
student1 = Student("Іван", 20, "Київський університет")

# додавання оцінок
student1.add_grade(85)
student1.add_grade(90)
student1.add_grade(78)

# зміна імені
student1.change_name("Петро")

# виведення інформації про студента та середню оцінку
print("Ім'я студента:", student1.name)
print("Вік студента:", student1.age)
print("Університет:", student1.university)
print("Список оцінок студента:", student1.grades)
print("Середня оцінка студента:", student1.calculate_average_grade())
