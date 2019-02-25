while True:
    try:
        n1 = int(input("enter first number : "))
        n2 = int(input("enter second number : "))    
        print(n1/n2)
        break

    except NameError:
        print("please input a digit")
    except ValueError:
        print("please input a digit")
    
    except ZeroDivisionError:
        print("second number cannot be zero")
