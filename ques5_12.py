from random import randrange
number=randrange(1  , 10)
score = 5
while score > 0:
    x= int(input())
    if x == number:
        score += 10
        break
    elif x > number:
        print("number is slight small of your expectation ")
    elif x < number:
        print("number is big than you expect")
    score -=1
print(score , number) 