import math


# Useful functions
def convert_str(input_str):
    input_str = str(input_str)
    if input_str.isdigit():
        return int(input_str)
    else:
        return float(input_str)


# ===================================== #
# ========  Exercise 1: Lists  ======== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 2 -- Exercise 1 --')
print('--------------------------------')

print('---  Exercise 1a & 1b: list  --- \n')

# 1a) Create a list of the days in a week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# 1b) Print all the items in the list
for i in days:
    print(i)


print('--------------------------------')

# 1c) Return the number of items in the list
print('-- Exercise 1c:  lists length -- \n')

print('= {}'.format(len(days)))

print('--------------------------------')
# 1d) Sort the items in ascending order (alphabetic)
print('--  Exercise 1d: sorted list  -- \n')

days.sort()

for j in days:
    print(j)

print('--------------------------------\n\n')

# ===================================== #
# ==== Exercise 2:  Formatted text ==== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 2 -- Exercise 2 --')
print('--------------------------------')

# 2a) Print the square root of π.
print('--  Exercise 2a:  sqrt of pi  -- \n')


def sqrt_pi():
    return math.sqrt(math.pi)


print('= {}'.format(sqrt_pi()))

print('--------------------------------')

# 2b) Include only 3 decimals
print('--  Exercise 2b:  3 decimals  -- \n')

print('= {0:.3f}'.format(sqrt_pi()))

print('--------------------------------')
# 2c) Include only 6 digits total
print('-- Exercise 2c:  6 digits tot -- \n')

print('= {:.6g}'.format(sqrt_pi()))


print('--------------------------------')
# 2d) Calculate the values to sin and cos for x in the interval [-1, 1] with step = 0.05.
# Print the result with a precision of 4 decimals in a table.
print('-- Exercise 2d: cos/sin table -- \n')


def calc_cos(a):
    return math.cos(a)


def calc_sin(b):
    return math.sin(b)


def print_table(step):
    print('      x  |   sin(x)  |   cos(x)  ')
    print('---------|-----------|---------- ')
    x = -1.00

    while x < 1.05:
        print('  {0: .2f}  |  {1: .4f}  |  {2: .4f}  '.format(x, calc_sin(x), calc_cos(x)))
        x += step


print_table(0.05)

print('--------------------------------\n\n')

# ===================================== #
# ======  Exercise 3:  Function  ====== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 2 -- Exercise 3 --')
print('--------------------------------')

print('--- Exercise 3: convert temp --- \n')
# 3) Create the function celsius_far that calculates the temperature from celsius to fahrenheit. Include user input.


def celsius_far(c):
    return c * (9/5) + 32


input_c = float(input('Enter temperature in Celsius: '))

print('{0:.4g} Celsius = {1:.4g} Fahrenheit'.format(input_c, celsius_far(input_c)))

print('--------------------------------\n\n')

# ===================================== #
# =====  Exercise 4:  Calculator  ===== #
# ===================================== #

print('--------------------------------')
print('-- Assignment 2 -- Exercise 4 --')
print('--------------------------------')
print('---  Exercise 4: calculator  --- \n')

# 4) Make a calculator that receives input (two numbers and +, - or *) from the user and print out the result.

input_d1 = convert_str(input('Enter number 1: '))
input_op = input('Enter an operator (+, - or *): ')
input_d2 = convert_str(input('Enter number 2: '))


def calc(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        print('Error: Not a valid operator')


print('{0} {2} {1} = {3}'.format(input_d1, input_d2, input_op, calc(input_d1, input_d2, input_op)))

print('--------------------------------')
