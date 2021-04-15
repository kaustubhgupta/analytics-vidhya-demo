def demo():
    age = int(input("Enter your age: ")) 
    year_exp = int(input("Enter your years of experience: ")) 
    
    if (age >= 16 and age <=20) and (year_exp <=1):
        print("Your Expected Salary: {}".format(10000))
    elif (age >= 21 and age <=26) and (year_exp >= 2 and year_exp <5):
        print("Your Expected Salary: {}".format(40000))
    elif (age >= 27) and (year_exp >=5):
        print("Your Expected Salary: {}".format(90000))
    else:
        print("Not in scoped rules!")

if __name__ == "__main__":
    demo()