terms=int(input("How many terms?\n"))

n1 = 0
n2 = 1
count = 0

if terms<=0:
          print("Enter postive integers")
elif terms == 1: 
    print(n1)
else:
    while  count<terms:
          print(n1,end=' , ')
          nth = n1+n2
          #update values
          n1=n2
          n2=nth
          count+=1
