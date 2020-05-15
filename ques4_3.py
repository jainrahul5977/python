x= int(input("Insert ht e temprature:"))
if x<-273.15:
    print("Invalid temprature")
elif x==273.15:
    print("freezing point")
elif x<0:
    print("temprature is below freezing point ")
else:
    if x==0:
        print("freezing point")
    elif x < 100:
        print("normal temprature")
    elif x==100 :
        print("boiling point")
    else:
        print("more than boiling point")