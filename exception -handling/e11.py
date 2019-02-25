a = [1, 2, 3, 4, 5]

i = 6
while True:
    try: 
        print(a[i])
        break

    except IndexError as err:
        print("Index error")
        print(err)
        #break

    else:
        i += 1
        print(i)

