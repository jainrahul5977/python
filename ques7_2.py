from random import randint
L = []
for i in range(50):
    L.append(randint(1,100))
print(L)
avg = sum(L)/len(L)
print(avg)
print(max(L) , min(L))
L.sort()
print(L[1] , L[-2])
count=0
for num in L:
    if num%2==0:
        count+=1
print(count)