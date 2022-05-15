class Hello:
    def __init__(self):
        print('Hello!')


class HelloWorld(Hello):
    def __init__(self):
        super().__init__()
        print('World!')


hw = HelloWorld()

print('-----------------')


class Class1:
    var = 20

    def __init__(self):
        self.var = 10


class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)


hw = Class2()

print('-----------------')


class Grandparent:
    def about(self):
        print('I am Grandparent')

    def about_myself(self):
        print('Actually, I am grandparent')


class Parent(Grandparent):
    def about_myself(self):
        print('Actually, I am parent')


class Child(Parent):
    def __init__(self):
        super().about()
        super().about_myself()


nick = Child()

print('-----------------')


class Computer:
    def calculate(self):
        print('Calculating...')


class Display:
    def display(self):
        print('I display the image on the screen')


class SmartPhone(Display, Computer):
    pass


iphone = SmartPhone()
iphone.calculate()
iphone.display()

print('-----------------')


class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128


class Display:
    def __init__(self):
        super().__init__()
        self.resolution = '8k'


class SmartPhone(Display, Computer):
    def print_info(self):
        print(self.memory)
        print(self.resolution)


iphone = SmartPhone()
iphone.print_info()



class Human:
    def about(self):
        print('I am Humana')

class Programmer(Human):
    def about_myself(self):
        print('Actually, I am programmer')
nick = Programmer()



