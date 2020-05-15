str = input("Enter a string")
l = []
l=str.split(" ")
for i in l:
    print(i[0].upper() + i[1:] , end = " ")
