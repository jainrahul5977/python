str = input("enter any statement.")
str=str.lower()
l=[]
l=str.split()
count=l.count("a")
count +=l.count("an")
count += l.count("the")
print(count)
