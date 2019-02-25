def FinallyTest():

    try: 
        x = int(input("first number  "))
        y = int(input("second number  "))
        print(x/y)
        return 1

    except Exception as err:
        print(err)
        return 0

    finally:
        print("it is finally clause")

result = FinallyTest()

print(result)
