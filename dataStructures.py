ListOfNumbers=[]
for i in range(1,11,2):
    ListOfNumbers.append(i)
# print(ListOfNumbers)

my_dict={
    "a":2,
    "b":15,
    "c":45
    }

for i in my_dict:
    print(i, "The value is:",my_dict[i])
    if my_dict[i]< 10:
        my_dict[i]=100
# print(my_dict)

my_set=set()
my_set.add(1)
my_set.add("geko")
print(my_set)




