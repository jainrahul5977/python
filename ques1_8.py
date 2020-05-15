#Write a program that asks the user to enter three numbers (use three separate input state-
#ments). Create variables called total and average that hold the sum and average of the
#three numbers and print out the values of total and average .

i=input("enter three number (space seprated):")
l=i.split(" ")
sum=0
for i in l:
    i=int(i)
    sum+=i
avg = sum/3
print(sum , avg , sep = " ")

