def findMinimum(*l):
    smallest=l[0]
    y=0
    idx=0
    for i in l:
        if i<smallest:
            smallest=l[y]
            idx=y
        
        else:
            pass
        y=y+1
        
    return smallest, idx

# a,b=findMinimum(1,432,63,1,2345,-43,32,1,0)
# print(a,b)


def checkTheBiggest(*l):
    count=0
    biggest=l[0]
    for i in l:
        if i>biggest:
            biggest=i
            idx=count
        else:
            pass
        count+=1
    print(biggest,idx)

# checkTheBiggest(3,3,5,35,3,2,32,43,423,42,3,33,56,4243242,23,535,23)

def tosortAsscendingorder(*l):
    n=len(l)
    sort=list(l)
    for i in range(n):
        for j in range(n):
            if sort[j]>sort[i]:
                tem=sort[i]
                sort[i]=sort[j]
                sort[j]=tem
            else:
                pass
    print(sort)
    
# tosortAsscendingorder(1,3,35,3,2342)

def tosortDeccendingorder(*t):
    sort=list(t)
    n=len(sort)
    for i in range(n-1):
        for j in range(i+1,n):
            if sort[j]<sort[i]:
                tem=sort[i]
                sort[i]=sort[j]
                sort[j]=tem
            else:
                pass
    print(sort)

# tosortDeccendingorder(1,432,543,5,24,2,42,4,)


def decendingOrder(*t):
    l=list(t)
    tempLargest=l[0]
    # n=len(l)-1
    for i in range(len(l)):
        for j in range(len(l)):
            if l[i]<l[j]:
                tempLargest=l[i]
                l[i]=l[j]
                l[j]=tempLargest
    return l, l[len(l)-1]

# l, a= decendingOrder(2,53,1,34,5,1,32,12)
# print(l, "is a list arraged and largest number is", a)

    
# text= "sushant parajuli"
# for i in text:
#     print(i, end=" ")

def toCheckIfItIsEmptyOrNot(l):
    if not(l):
        return "empty"
    else:
        return "not-empty"

listt=[1,34,2,4,24]
blah=[]

tuplee=()
dictt={}

print(toCheckIfItIsEmptyOrNot(tuplee))
print(toCheckIfItIsEmptyOrNot(dictt))
print(toCheckIfItIsEmptyOrNot(blah))
print(toCheckIfItIsEmptyOrNot(listt))



    
    



