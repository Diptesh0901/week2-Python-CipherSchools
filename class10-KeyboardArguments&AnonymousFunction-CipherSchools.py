def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)

def func(a, b, c):
    print(a)
    print(b)
    print(c)

def hello():
    print("Hello World !")
    return 1

a = 1
type(hello)

a = hello

hello = 2
print(hello)

print(a())

def func():
    print("hello")

def func(a):
    print(a)

def func(a,b,c):
    print(a)
    print(b)
    print(c)

func(c = 1, a = 2, b = 3)

hello = 2
print(hello)

# *args **kwargs

# ARGUMENTS IN PYTHON -->

# required positional arguments
# default arguments
# optional arguments
# optional keyworded ony arguments
# default keyworded only arguments
# required keyworded only arguments


def func(a, b):
    print(a, b)

func (1, 2)

def func(a = 1, b = 2):
    print(a, b)

func()
func(1)
func(3, 4)

def func(*c):
    print(c)

func()

def func(a, b, *c, d, e ="jatin"):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)

func(1, 2, 3, 4, 5, 6, 7, d = "something", e = "asdf")

def func(a, b = 1, *c, d , e = "", **k):
    print(k)

# Anonymous function or lambda functions

lambda a, b: a + b
a(1,2)

