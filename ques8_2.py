str = input("enter space seprated number")
l = str.split()
sum=0
for item in l:
    sum +=int(item)
print(sum)