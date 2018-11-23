from flask import Flask
app = Flask(__name__)


# ===================================== #
# ==    Exercise 1: Install Flask    == #
# ===================================== #

print('--------------------------------')
print('-- Assignment 4 -- Exercise 1 --')
print('--------------------------------')

# 1)  Install Flask and create a simple program that shows the following in the browser:
#     "Dette er mitt første program med Flask"
print('-- Exercise 1:  Install Flask -- \n')


@app.route('/')
def basic_flask():
    return 'Dette er mitt første program med Flask'


if __name__ == '__main__':
    app.run()

