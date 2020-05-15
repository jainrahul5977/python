from math import pow
count=0
for i in range(1 , 100):
    sq=i**2
    if sq%10 == 1:
        count=count+1
print(count , "square are ends with 1 ")