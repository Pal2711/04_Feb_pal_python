age=int(input("Enter Your age : "))
weight = int(input("Enter yout Weight : "))

if(age>18):
    if(weight>=50):
        print("Your are eligible to donate blood ")
    else:
        print("Sorry your weight is lessthen 50Kg")
else:
    print("Sorry your age is below 18 ")