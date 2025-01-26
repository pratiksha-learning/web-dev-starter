class Employee:
    def __init__(self, name, age, salary, profession):
        self.name = name
        self.age = age
        self.profession = profession
        self.salary = salary
    def increase_salary(self, parcent):
        self.salary += self.salary * (parcent/100)

    # there is no need to have function to print if we use __str__ method 
    # __str__ method is used to return string sentences
    def __str__(self):
        return f"{self.name} is {self.age} and has a profession of {self.profession} with the salary of {self.salary}"

employee1 = Employee('pratiksha', 24, 500000, 'developer')
print(employee1)