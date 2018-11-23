import math


def convert_str(input_str):
    input_str = str(input_str)
    if input_str.isdigit():
        return int(input_str)
    else:
        return float(input_str)


# ===================================== #
# =======  Exercise 1:  Output  ======= #
# ===================================== #

print('--------------------------------')
print('-- Assignment 1 -- Exercise 1 --')
print('--------------------------------')

print('--  Exercise 1a: hello world  -- \n')

# a) Print «Hello, world!»
print('Hello, world!')


print('--------------------------------')
# b) Print «Hello, -name-!». For example: «Hello, Ole!».
print('--  Exercise 1b: hello, name  -- \n')

name = 'Ingvild'
print('Hello, ' + name + '!')


print('--------------------------------')
# c) Read the users input and print it in a formatted output.
print('-- Exercise 1c:  hello, input -- \n')

input_name = input('Enter your name: ')

print('Hello, {}!'.format(input_name))

print('--------------------------------\n\n')

# ===================================== #
# =====  Exercise 2:  Basic math  ===== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 1 -- Exercise 2 --')
print('--------------------------------')

print('--  Exercise 2a:  basic math  -- \n')
# a) Calculate 1 + 3 * 3


def a():
    return 1 + 3 * 3


print('1 + 3 * 3 = {}'.format(a()))


print('--------------------------------')
# b) Calculate 1 + (5 * 3)
print('--  Exercise 2b:  basic math  -- \n')


def b():
    return 1 + (5 * 3)


print('1 + (5 * 3) = {}'.format(b()))


print('--------------------------------')
# c) Calculate (1 + 4) * 3
print('--  Exercise 2c:  basic math  -- \n')


def c():
    return (1 + 4) * 3


print('(1 + 4) * 3 = {}'.format(c()))


print('--------------------------------')
# d) Area and circumference to a circle with radius 8
print('-- Exercise 2d:  circle (r=8) -- \n')


def circle_area(radius):
    return math.pi * (radius**2)


def circle_circumference(radius):
    return 2 * math.pi * radius


r = 8

print('Area: {}'.format(circle_area(r)))
print('Circumference: {}'.format(circle_circumference(r)))

print('--------------------------------\n\n')

# ===================================== #
# ======  Exercise 3: More math  ====== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 1 -- Exercise 3 --')
print('--------------------------------')

print('---  Exercise 3:  more math  --- \n')
# Read two numbers from the user, sum them, and print the result.


def calc(x, y):
    return x + y


print('The sum of two numbers\n')

input_x = convert_str(input('Enter number 1: '))
input_y = convert_str(input('Enter number 2: '))

print('{0} + {1} = {2}'.format(input_x, input_y, calc(input_x, input_y)))


print('--------------------------------')
