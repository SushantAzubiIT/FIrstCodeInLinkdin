def helloPrinterNoOfTimes():
    n=int(input("Enter how many times you wanna print hello world for your file :"))
    for i in range(n):
        print("hello World", end="\t")
    print("   ") 
# helloPrinterNoOfTimes()

def addTillInfinity(*adder):
    total=0
    for i in adder:
        total= total+ i
    return total

# b=addTillInfinity(3,4,5,6,23,4,6,546,6,4564,6)
# print(b)