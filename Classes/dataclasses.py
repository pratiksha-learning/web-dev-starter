from dataclasses import dataclass
@dataclass
class Project:
    name: str
    age: int
    project: str

class Developer:
    def __init__(self, name, age, project):
        self.name = name
        self.age = age
        self.project = project

    def __repr__(self):
        return f"Developer class(name={self.name}, age={self.age}, project={self.project})"
    
project = Project('prat', '24', 'Onion')
developer = Developer('prat', '24', project)

print(developer)