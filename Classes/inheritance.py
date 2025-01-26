class Employee:
    def __init__(self, name, age, salary, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.salary = salary
    def info(self):
        print(f"{self.name} is {self.age} and has a profession of {self.profession} with the salary of {self.salary}")

class Developer(Employee):
    def increase_salary(self, parcent):
        self.salary += self.salary * (parcent/100)


employee1 = Employee('pratiksha', 24, 500000, 'developer')
developer = Developer('Prat', '24', 100000, 'Developer')
developer.increase_salary(20)
developer.info()