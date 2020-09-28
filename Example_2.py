"""
CSE310 Python Workshop - Example 2

This example will explore functions in Python
"""

"""
Example 1 - Function to return the average of a 
list of numbers
"""
def average_numbers(numbers):
    if len(numbers) > 0:
        avg = sum(numbers) / len(numbers)
        return avg
    else:
        return 0
print("average = {}".format(average_numbers([3,1,2,7])))
print()

"""
Example 2 - Function to prompt user for a word and 
display the word 'encoded'.  Encoding is done by 
shifting each letter to the right one.
"""
word = input("Enter a word: ")
def show_code(word):
    new_word = ""
    for ltr in word:
        new_word += chr(ord(ltr) + 1)
    return new_word
result = show_code(word)
print("result = {}".format(result))  # Show that 'None' is returned
print()

"""
Example 3 - Function to calculate area and perimeter
of a rectangle and return both values.
"""
def rectangle_calc(side, base):
    perimeter = (side * 2 + base * 2)
    area = side * base
    return area, perimeter
my_area, my_perim = rectangle_calc(3,4)
print("Area = {}  Perim = {}".format(my_area, my_perim))
print()

"""
Example 4 - Function to calculate a price with optional
tax and discount parameters.  If not provided, tax should
be 5% and discount should be zero. 
"""
def calc_price(base_price, tax = .5, discount = 0):
    price = (base_price - discount) * (tax + 1)
    return price

print("price1: ${:.2f}".format(calc_price(3.00, 0.01, 1.00)))
print("price2: ${:.2f}".format(calc_price(3.00, 0.01)))
print("price3: ${:.2f}".format(calc_price(3.00)))
print("price4: ${:.2f}".format(calc_price(3.00, discount=2.00)))
print("price5: ${:.2f}".format(calc_price(base_price=3.00, tax=0.01, discount=1.00)))