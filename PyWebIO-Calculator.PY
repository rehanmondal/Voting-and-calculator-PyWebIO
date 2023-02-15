from pywebio.input import *
from pywebio.output import *

import time  

def calculator():
    n1 = int(input("Enter first number : ", type=NUMBER))
    n2 = int(input("Enter second number : ", type=NUMBER))

    operation = radio("Choose an operator",options=['+','*','-','/'])

    if operation=='+':
        put_text("The result of Addition is : ",n1+n2)

    elif operation=='-':
        put_text("The result of Substraction is : ",n1-n2)

    elif operation=='*':
        put_text("The result of Multiplication is : ",n1*n2).style('color:green')

    elif operation=='/':
        with put_loading():
            put_text("Showing Results...")
            time.sleep(2)  # Some time-consuming operations
            # put_text("The answer of the universe is 42")
            style(put_text("The result of Division is : ",n1/n2),'color:green')

calculator()




# .style('width:4rem; height:4rem')

'''
# for shape in ('border', 'grow'):
#     for color in ('primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark'):
#         put_text(shape, color)
#         put_loading(shape=shape, color=color)


# for shape in ('border', 'grow'):
# for color in ('primary','secondary', 'success'):
put_loading(color='primary')



import time  

with put_loading():
    put_text("Start waiting...")
    time.sleep(3)  # Some time-consuming operations
put_text("The answer of the universe is 42")

'''