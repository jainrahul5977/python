from math import log
x= int(input("insert the vadriable: "))
sum=0
for i in range(1 , x+1):
    sum=sum + (1/i)
print((sum-log(x)))