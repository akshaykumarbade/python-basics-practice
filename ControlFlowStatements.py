# if-elfi-else statement
a = 55
# int(input("Enter an integer: "))

if a < 0:
    print("Please enter a positve integer...")
elif a == 0:
    print("You entered 0")
elif a < 100:
    print("You entered an integer less than 100 but greater than 0")
else:
    print("you entered integer greater than 100..")

# for statement
words = ["Love", "Hate", "Trust", "Care", "Money", "Power"]
for w in words:
    print(w, len(w))
else:
    print("no item left...")

print('')

bucket = (4, "Nina", "Greece", "Student", 24.90)
for item in bucket:
    print(item)

employee = {'Novo': 'current', 'Joey': 'former',
            'Jarvis': 'current', 'Taylor': "Current"}
print(employee)


# while loop
i = 1
n = 6

while i <= n:
    print(i)
    i = i+1

# continue and break

x = 1
while x <= 10:
    print("5 * ", x, " = ", 5*x)
    if x >= 5:
        break

    x = x+1

num = 0
while num < 10:
    num += 1
    if (num % 2) == 0:
        continue
    print(num)


z = 11
if (z > 11):
    pass
print("hello world")
