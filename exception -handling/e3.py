try:
    n1 = int(input("enter first number : "))
    n2 = int(input("enter second number : "))    
    print(n1/n2)

except ZeroDivisionError as err:
    print("second number cannot be zero")
    print(err)

