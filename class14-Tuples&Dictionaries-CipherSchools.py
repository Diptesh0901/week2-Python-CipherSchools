# TUPLES -->

a = (1, 2, 3, 4)
print(type(a))

def func(*args):
    print(type(args))

func(1, 2, 3, 4)

a = 5
b = 9

a, b = b, a
c = a, b
print(type(c))

def sum_diff(a, b):
    s = a+b
    d = a-b

    return s, d

c = sum_diff(10, 5)
print(type(c))
print(c)

a = 1, 2, 3, 4
print(type(a))

s, d = sum_diff(10, 5)
print(s, d)

# LIST TO TUPLE AND TUPLE TO LIST -->

a = (1, 2, 3, 4)
print(list(range(5)))

print(tuple(range(5)))

# RETURNING MULTIPLE VALUES FROM FUNCTION -->

a = (1, 2, 3, 4)
a = [1, 2, 3, 4]
a.append(5)
print(a)
a.append(7)
print(a)

# DICTIONARIES -->

a = [1, 2, 3, 4, 5]
print(a[0])

a = dict()

a = {
     "name": "Jatin Katyal",
     1: "something",
     (1, 2): "tuple key wat?"

}

a["name"]

a=["name"]

a = {
    "name": "Jatin Katyal"
}

a["name"] = "Gourav"
print(a)

a = {
    "name": "jatin",
    "company": "shuttle",
     "college": "IPU"
}

key = "marks"
if key in a:
    print(a[key])
else:
    print("key doesn't exist")

key = "marks"
print(a.get(key, "key doesn't exist"))

print(a.values())

for key, value in a.items():
    print(key, "->", value)

for x in a:
    print(x)

print(list(a))



