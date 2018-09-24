from calculator import addition
from calculator import subtraction
from calculator import multiplication
from calculator import division

__author__ = 'TheRusher28'
__mantainer__ = 'TheRusher28'
__email__ = 'therusher28@gmail.com'
__status__ = 'Beginner'

num_uno = input('Please, type the first number of your operation :')
num_dos = input('Please, type the second number of your operation :')
operation = input('What operation do you need? ')
if operation == 'addition':
    print(addition(float(num_uno), float(num_dos)))
elif operation == 'subtraction':
    print(subtraction(float(num_uno), float(num_dos)))
elif operation == 'multiplication':
    print(multiplication(float(num_uno), float(num_dos)))
elif operation == 'division':
    print(division(float(num_uno), float(num_dos)))
