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
            style(put_text("The result of Division is : ",n1/n2),'color:green')

calculator()

