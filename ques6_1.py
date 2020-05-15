str = input("Enter the string")
print("a " , len(str))
print("b" , str*10)
print(str[0])
print(str[:3])
print(str[-3:])
print(str[::-1])
if len(str) > 7:
    print(str[6])
else :
    print("string is not enough big")
print(str[1:-1])
print(str.replace('a' , 'e'))
for i in range(len(str)):
    print(end=" ")