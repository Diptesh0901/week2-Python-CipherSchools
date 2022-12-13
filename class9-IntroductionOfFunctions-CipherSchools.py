# Function

x = 6
x = "jatin"
x = 1.5
x = print

def show_loading():
    for i in range(3):
        print("loading", ","*(i+1))

show_loading()

a = 5
b = 7

print(a+b)
print("loading...")
print("loading...")
print("loading...")

print(a-b)
print("loading...")
print("loading...")
print("loading...")

print(a*b)
print("loading...")
print("loading...")
print("loading...")

print(a+b)
show_loading()

print(a-b)
show_loading()

print(a*b)
show_loading()

def sheldon_knock(name):
    for _ in range(3):
        print("knock knock knock", name)

sheldon_knock("leonard")

def sheldon_knock(name, times = 3):
    for _ in range(times):
        print("knock knock knock", name)