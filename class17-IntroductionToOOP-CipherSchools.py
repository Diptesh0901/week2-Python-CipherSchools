# Object Oriented Programming

# abstraction = need to know basis

student1 = {
    "name": "jatin katyal",
    "marks": 50
}

student2 = {
    "name": "Samarth",
    "marks": 100
}

print()

# python object can have multiple attributes
# classes are callables

class Person:
    pass

p = Person()
print(p)

print(hex(id(p)))

a = 1

class Person:
    def say_hi(self):
        self.name = 'Nikhil'
        print('Hello, how are you' + self.name + "?")

p = Person()
p.say_hi()

class Person:
    name = "Jatin"

    def say_hi(this):
        print(f"Hello Everyone : I am {this.name}")

p = Person()
Person.say_hi(p)
