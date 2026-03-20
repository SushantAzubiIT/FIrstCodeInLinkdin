import random

a=int(input("what range u wanna start ur game from :"))
n=int(input("Till what range u wanna go ending point :"))
randomNumber=random.randint(a,n)

user_guess=int(input(f"enter your guess within your range of {a}, to {n}."))
while True:
    if (user_guess==randomNumber):
        print("you guessed it right")
        break
    else:
        if user_guess<randomNumber:
            print("guess again the number is higher then ur previous guess")
            user_guess=int(input("enter your guess :"))
        else:
            print("guess again the number is lower then ur previous guess")
            user_guess=int(input("enter your guess :"))



import random
rangeOfNumber= input("enter from what number to what number u want range to go like 10-20 seprated by - :")
a=rangeOfNumber.split("-")

randomNumber=random.randint(int(a[0]), int(a[1]))

user_guess=int(input(f"enter your guess within your range of {a[0]}, to {a[1]}."))
while True:
    if (user_guess==randomNumber):
        print("you guessed it right")
        break
    else:
        if user_guess<randomNumber:
            print("guess again the number is higher then ur previous guess")
            user_guess=int(input("enter your guess :"))
        else:
            print("guess again the number is lower then ur previous guess")
            user_guess=int(input("enter your guess :"))




#
# practice of map and a for loop that can convert each data type into another 
#

array=["2", "2", "36", "72"]

arrayInt=list(map(int,array))
print(arrayInt)

# another way
arrayInt2=[]
for x in array:
    inted=int(x)
    arrayInt2.append(inted)

print(arrayInt2)

#here is one liner of that another way

arrayInt3= [int(x) for x in array]
print(arrayInt3)