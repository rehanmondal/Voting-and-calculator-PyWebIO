from pywebio.input import *
from pywebio.output import *

def Voting():
    name = input("Enter Name : ", type='text')
    age = int(input("Enter Age : ", type=NUMBER))

    if age>=18 and age<100:
        style(put_text("Check your Details Here :- "),'color:Blue')
        put_table([['NAME','AGE'],[name,age]])
        check = checkbox(options=["All the details are right ?"])

        if check:
            selection = radio("Vote for a Language : ",options=['PYTHON','JAVA','C++','C'])
            style(put_text("THANKS FOR YOUR VOTE ! We will announce results soon .."),'color:blue')
            keep_voting = radio("Continue Voting ?",options=['Yes','No'])
            if keep_voting == 'Yes':
                Voting()
            else:
                return style(put_text("Voting Ended ,You have succesfully Logged out.. "),'color:green')
        elif check=='Reset':
            Voting()

    else:
        style(put_text("You are not elligible to vote "),'color:red')

Voting()
