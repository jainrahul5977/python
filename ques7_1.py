l = eval(input("enter the list"))
print("a " , len(l))
print("b" , l[-1])
print("c" , l.reverse())
if 5 in l:
    print("yes")
else :
    print("no")
print(l.count(5))
l.pop(0)
l.pop(-1)
l.sort()
print(l)
count=0
for item in l:
    if item<5:
        count+=1

print(count)
