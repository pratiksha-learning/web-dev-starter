class Employee:
    def __init__(self, name, age, project):
        self.name = name
        self.age = age
        self.project = project
    
    @property
    def get_name(self):
        pass

class Developer(Employee):
    def get_name(self):
        return self.name

d = Developer('Prat', '20', 'kkk')
print(d.get_name())