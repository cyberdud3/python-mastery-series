try: 
    f = open('text.txt')
    for line in f:
        print(line, end='')

except IOError:
    print('cannot open file')
finally:
    f.close()
