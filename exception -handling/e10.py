while True:
    try:
        n1 = int(input("enter first number : "))
        n2 = int(input("enter second number : "))    
        print(n1/n2)

    except Exception as err:
        print(err)

    else:
        break
