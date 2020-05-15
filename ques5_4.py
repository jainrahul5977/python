from math import pow
x= int(input("insert the number: "))
sum=0
for i in range(1 , x+1):
    sum +=int(-(pow(-1 , i)*i))
print(sum)