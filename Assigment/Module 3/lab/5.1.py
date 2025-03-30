try:
    num = int(input("Enter a number: "))
    print(10 / num)  
    my_list = [1, 2, 3]
    print(my_list[5])
except (ZeroDivisionError, IndexError, ValueError):
    print("An error occurred!")
