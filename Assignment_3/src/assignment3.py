# Useful functions
def convert_str(input_str):
    input_str = str(input_str)
    if input_str.isdigit():
        return int(input_str)
    else:
        return float(input_str)


# ===================================== #
# ==      Exercise 1: Files I/O      == #
# ===================================== #

print('--------------------------------')
print('-- Assignment 3 -- Exercise 1 --')
print('--------------------------------')

# a)  Write three lines to a file
print('-- Exercise 1a: write to file -- \n')

# List with the lines to write
lines_list = ['Hallo\n', 'Skriver en linje til\n', 'Her kommer enda en linje\n']


def write_to_file():
    try:
        f_write = open(r'..\file1.txt', 'a+')
    except IOError:
        print('Error: Kan ikke åpne file1.txt')
    else:
        f_write.writelines(lines_list)
    finally:
        f_write.close()


# f_write = open('file1.txt', 'wt')
# f_write.write('Hello\n')
# f_write.close()

# f_append = open('file1.txt', 'at')
# f_append.write('Writing a new line\n')
# f_append.write('Here comes another line')
# f_append.close()

print('--------------------------------')
# b)  Read line #2 from the file
print('---  Exercise 1b: read line  --- \n')

f_read = open('file1.txt', 'rt')
f_read.readline()
print(f_read.readline())
f_read.close()

print('--------------------------------')
# c)  Read and print the 10 first letters from the file
print('-- Exercise 1c: read letters -- \n')

f_read = open('file1.txt', 'rt')
print(f_read.read(10))
f_read.close()

print('-------------------------------- \n\n')

# ===================================== #
# == Exercise 2: Basic file handling == #
# ===================================== #

print('--------------------------------')
print('-- Assignment 3 -- Exercise 2 --')
print('--------------------------------')

# 2)  Create a function that counts the number of lines and words in a file.
print('-- Exercise 2:  file handling -- \n')


# def get_file_content():
#     f = open('file1.txt', 'r')
#
#     for lines in f:
#         lines
#     words = f.read()
#     f.close()


print('-------------------------------- \n\n')

# ===================================== #
# == Exercise 3:  More file handling == #
# ===================================== #

print('--------------------------------')
print('-- Assignment 3 -- Exercise 3 --')
print('--------------------------------')

# 3)  Create a function that accepts a filename as an argument,
#     and returns the number of characters/bytes of the content.
print('-- Exercise 3:  file handling -- \n')


def get_file(file_name):
    f = open(file_name, 'r')

    characters = []
    for char in f:
        characters.append(char)
    f.close()
    return len(characters)


print('--------------------------------')
