count = 0
try:
    f = open('text.txt')
    while True:
        c = f.read(1)
        if not c:
            print('\nend of file')
            break
        if c == ' ' or '\n':
            count += 1

except IOError as err:
    print('cannot open file')
    print(err)
finally:
    print(count+1)
    f.close()
