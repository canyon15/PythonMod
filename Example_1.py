"""
CSE310 Python Workshop - Example 1

This example will explore variables, expressions, conditions, 
data structures, and loops in Python
"""

# Python Variables

w = True
x = 5
y = "cat"
z = 3.14
print(w, x, y, z)
print()

# Convert Variables

w = str(6)
x = int("5")
y = float("3.14")
z = int(3.14)
print(w, x, y, z)
print()

# Inputs & Expressions

num = int(input("Enter a number: "))
print("+ 1 = {}".format(num + 1))
print("- 1 = {}".format(num - 1))
print("* 2 = {}".format(num * 2))
print("/ 3 = {}".format(num / 3))
print("// 3 = {}".format(num // 3))
print("% 3 = {}".format(num % 3))
print("** 3 = {}".format(num ** 3))

num += 1

print("+= 1 => {}".format(num))

num *= 2
print("*= 2 => {}".format(num))
print()

# Conditions

temp = float(input("Enter the water temp: "))
if temp >= 212:
    print("Gas")
elif temp > 32:
    print("Liquid")
else:
    print("Solid")

print()

# Lists (Dynamic Arrays)

numbers = [20, 13, 7, 22]
print("numbers = {}".format(numbers))

numbers.append(53)
print("after appending = {}".format(numbers))

print("first number = {}".format(numbers[0]))
print("fourth number = {}".format(numbers[3]))
print("length = {}".format(len(numbers)))

del numbers[1]
print("after deleting 2nd = {}".format(numbers))
print()

# Dictionaries (Maps)

observation = {"temp" : 45.3, "sky" : "rain", "wind": "storm"}
print(observation)

print("sky: {}".format(observation["sky"]))

observation["wind"] = "spren"
print("after updating wind: {}".format(observation))
print()

# Loops

word = input("Enter a word: ")
for ltr in word:
    print(ltr)

count = int(input("Enter a number: "))
for x in range(count):
    print(x)

size = int(input("How many even numbers do you want: "))
numbers = [2*x for x in range(size)]
print(numbers)

multiple = int(input("Find multiples of what in your list: "))
for num in numbers:
    if num % multiple == 0:
        if num != 0:
            print(num)