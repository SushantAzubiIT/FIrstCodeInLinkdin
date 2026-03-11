def addTillInfinity(*adder):
    """This take input in Array adder since * is used in argument of function
       Then it will add all those numbers"""
    total=0
    for i in adder:
        total= total+ i
    return total

b=addTillInfinity(3,4,5,6,23,4,6,546,6,4564,6)
print(b)
