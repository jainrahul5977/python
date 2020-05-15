from random import randint
l=[randint(0 , 1) for i in range(100)]
frequency = [0]
j=0
for i in  l:
    if i==1:
        j+=1
        frequency.append(0)
    else:
        frequency[j]+=1
print(max(frequency))
print(l)