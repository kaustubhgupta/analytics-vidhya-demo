from pywebio.input import input, NUMBER
from pywebio.output import put_text
from pywebio.exceptions import SessionClosedException

def demo():
    age = input("Enter your age: ", type=NUMBER)
    year_exp = input("Enter your years of experience: ", type=NUMBER)
    
    if (age >= 16 and age <=20) and (year_exp <=1):
        put_text("Your Expected Salary: {}".format(10000))
    elif (age >= 21 and age <=26) and (year_exp >= 2 and year_exp <5):
        put_text("Your Expected Salary: {}".format(40000))
    elif (age >= 27) and (year_exp >=5):
        put_text("Your Expected Salary: {}".format(90000))
    else:
        put_text("Not in scoped rules!")

if __name__ == "__main__":
    try:
        demo()
    except SessionClosedException:
        print("The session was closed unexpectedly")