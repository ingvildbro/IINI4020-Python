# Prints formatted output 'Assignment X -- Exercise Y'
def format_a_e_output(a, e):
    print('------------------------------------')
    print('---  Assignment {0} -- Exercise {1}  ---'.format(a, e))
    print('------------------------------------')


# ========================================= #
# ====      Exercise 1: Files I/O      ==== #
# ========================================= #

# a)  Write three lines to a file
def write_lines_to_file():
    # List with the lines to write
    lines_list = ['Hallo\n', 'Skriver en linje til\n', 'Her kommer enda en linje\n']

    try:
        f_write = open('file1.txt', 'a+')
    except OSError:
        print('Error: Could not open file1.txt')
    else:
        f_write.writelines(lines_list)
        f_write.close()


# b)  Read line #2 from the file
def read_line_nr2():
    try:
        f = open('file1.txt', 'r')
    except OSError:
        print('Error: Could not open file1.txt')
    else:
        print('File: {}'.format(f.name))  # Name of file read
        f_lines = f.readlines()
        print('Line nr. 2: {}'.format(f_lines[1]))
        f.close()


# c)  Read and print the 10 first letters from the file
def read_first_10_chars():
    try:
        f = open('file1.txt', 'r')
    except OSError:
        print('Error: Could not open file1.txt')
    else:
        print('File: {}'.format(f.name))    # Name of file read
        f_content = f.read()
        print('First 10 characters: {}'.format(f_content[0:11]))
        f.close()


# ========================================= #
# ==== Exercise 2: Basic file handling ==== #
# ========================================= #

# 2)  Create a function that counts the number of lines and words in a file.
def lines_and_words_length():
    try:
        f = open('file1.txt', 'r')
    except OSError:
        print('Error: could not open file1.txt')
    else:
        print('File: {}'.format(f.name))  # Name of file read
        f_lines = f.readlines()

        f_words = []
        for line in f_lines:
            f_words.append(line.split())

        print('Number of lines total: {}'.format(f_lines))
        print('Number of words total: {}'.format(len(f_words)))
        f.close()


# ========================================= #
# ==== Exercise 3:  More file handling ==== #
# ========================================= #

# 3)  Create a function that accepts a filename as an argument,
#     and returns the number of characters/bytes of the content.


def chars_from_filename(file_name):
    print('File: {}'.format(file_name))
    # Characters
    try:
        f_chars = open(file_name, 'rt')
    except OSError:
        print('Error: could not open {}'.format(file_name))
    else:
        char_list = f_chars.read()
        print('Number of characters total: {}'.format(len(char_list)))
        f_chars.close()


def bytes_from_filename(file_name):
    try:
        f_bytes = open(file_name, 'rb')
    except OSError:
        print('Error: could not open {}'.format(file_name))
    else:
        bytes_list = f_bytes.read()
        print('Number of bytes total: {}'.format(len(bytes_list)))
        f_bytes.close()


def format_ex(ex_nr, ex_name):
    str_ex = 'Exercise ' + ex_nr + ':'

    if len(ex_nr) == 1:
        str_ex += ' '


if __name__ == '__main__':
    format_a_e_output(3, 1)
    print('---  Exercise 1a: write to file  --- \n')
    write_lines_to_file()
    print('------------------------------------ \n\n')

    print('--- Exercise 1b: read line nr. 2 --- \n')
    read_line_nr2()
    print('------------------------------------ \n\n')

    print('---  Exercise 1c:  read letters  --- \n')
    read_first_10_chars()
    print('------------------------------------ \n\n')

    format_a_e_output(3, 2)
    print('---  Exercise 2:  file handling  --- \n')
    lines_and_words_length()
    print('------------------------------------ \n\n')

    # 3) chars and bytes from file
    format_a_e_output(3, 3)
    print('-- Exercise 3: more file handling -- \n')
    chars_from_filename('file2.txt')
    bytes_from_filename('file2.txt')
    print('------------------------------------')
