from math import sqrt
x=int(input("insert number to check is perfect : "))
l=[]

check=0
for i in range(2 , x):
    if x%i==0:
        l.append(i)n
for i in l:
    if int(sqrt(i))== int(sqrt(i)+.999) :
        print(x , "is a perfect number.")