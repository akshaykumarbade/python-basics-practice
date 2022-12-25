"""
This program prints Hello World.
"""
# pylint disable=C0103
message = "Hello World"
print(message)


x = 2
y = 3


def sum():
    sum = x+y
    return sum


print(sum())


counter = 100
_count = 100
name1 = "Zara"
name2 = "Nuha"
Age = 20
zara_salary = 100000

print(counter)
print(_count)
print(name1)
print(name2)
print(Age)
print(zara_salary)

list = [4, 'Akshay', 26.5, 50000, 'Pune']
print(list)

tuple = (5, 'Komal', 25, 40000, 'Pune', 5.5)
print(tuple)

for i in range(5):
    print(i)

for i in range(1, 6):
    print(i)

mydic = {'name': 'Nina', 'age': '25', 'country': 'Greece'}
print(mydic)
print(mydic.keys())
print(mydic.values())


a, b = True, False
print(a)
print(type(a))
print(b)
print(type(b))


n = int(5.56)
n1 = int("6")
print(n)
print(n1)

print(6 == 5)

a += 5
print(a)

var = 100
if (var == 100):
    print('Hello')
print("Hrllo")
# del var
print(var)
