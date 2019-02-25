try:
    n1 = int(input("enter first number : "))
    n2 = int(input("enter second number : "))    
    print(n1/n2)

except ValueError:
    print("please input a digit")
    
except ZeroDivisionError:
    print("second number cannot be zero")

