from pywebio.input import input_group, input, NUMBER
from pywebio.output import put_text
from pywebio.exceptions import SessionClosedException

def demo():

    inputs = input_group("Salary Prediction", [
        input("Enter your age: ", type=NUMBER, name='age'),
        input("Enter your years of experience: ", type=NUMBER, name="year_exp")
    ])
    
    if (inputs["age"] >= 16 and inputs["age"] <=20) and (inputs["year_exp"] <=1):
        put_text("Your Expected Salary: {}".format(10000))
    elif (inputs["age"] >= 21 and inputs["age"] <=26) and (inputs["year_exp"] >= 2 and inputs["year_exp"] <5):
        put_text("Your Expected Salary: {}".format(40000))
    elif (inputs["age"] >= 27) and (inputs["year_exp"] >=5):
        put_text("Your Expected Salary: {}".format(90000))
    else:
        put_text("Not in scoped rules!")

if __name__ == "__main__":
    try:
        demo()
    except SessionClosedException:
        print("The session was closed unexpectedly")