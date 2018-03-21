class Person(object):
    def __init__(self, name, education):
        self.name = name
        self.education = education

    def work(self):
        print("%s goes to work." % self.name)


class Employee(Person):
    def __init__(self, education, job, name):
        super(Employee, self).__init__(name, education)
        self.job = job

    def work(self):
        Person.work(self)


class Programmer(Employee):
    def __init__(self, education, name, pay):
        super(Programmer, self).__init__(education, 'Programmer', name)
        self.pay = pay

    def program(self):
        print("%s programs a game." % self.name)


bob = Person('Bob', 'Highschool Graduate')
june = Employee('Bachelor\'s Degree', 'McDonalds Cashier', 'June')
june.work()
kee = Programmer('Master\'s Degree', 'Kee', "$ 79,530")
kee.program()

# Denim Xiong
