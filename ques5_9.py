s = set()
i=1
while(i**2 <=1000):
    s.add(i**2)
    i+=1
i=1
while(i**3 <=1000):
    s.add(i**3)
    i+=1
i=1
while(i**5 <=1000):
    s.add(i**5)
    i+=1
count=0
for i in range(1 , 1001):
    if i not in s:
        count+=1
print(count)
print(s)