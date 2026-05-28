class Person:
    
    def __init__(self,name,lastname):
        self.name=name
        self.last=lastname 

    def get_name(self):
        return f'{self.name} {self.last}'
    
    def set_name(self,name,lastname):
        self.name=name 
        self.lastname=lastname


class salary(Person):

    def __init__(self, name, lastname, salary):
        super().__init__(name, lastname)
        self.salary=salary

    def get_salary(self):
        return f'salary: {self.salary}'


    def set_salary(self,salary):
        self.salary=salary 


per1=salary('amruth','pai',2500)
print(per1.get_salary())
per1.set_salary(3500)
print(per1.get_salary(),per1.get_name())

  
