class Employee:
    def __init__(self, name, age, salary, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.salary = salary
    def increase_salary(self, parcent):
        self.salary += self.salary * (parcent/100)
    def info(self):
        print(f"{self.name} is {self.age} and has a profession of {self.profession} with the salary of {self.salary}")

employee1 = Employee('pratiksha', 24, 500000, 'developer')
employee1.increase_salary(20)
employee1.info()