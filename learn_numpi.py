import numpy as np
result=np.random.permutation(np.arange(10))
# print(result)

a=np.random.rand(1000);
# print(a)

import matplotlib.pyplot as plt
plt.hist(a, bins=100)
# plt.show()


b=np.random.rand(100000)
plt.hist(b,bins=200)

# plt.show()

c=np.random.rand(2,3)
# print(c)

d=np.random.rand(1,2,3,4)
# print(d)
# print(d.ndim)

reshaper= np.arange(100).reshape(4,25)
# print(reshaper)

normal_list=[1,2,42,12,24,65]
sliced=normal_list[2:5]
print(sliced)

sliced[0]=4567
print(sliced)
print(normal_list)

# now trying with array of np
test_array=np.array(normal_list)
print(test_array)
test_newarray=test_array[2:5]
print(test_newarray)
test_newarray[0]=2
print(test_newarray)
print(test_array)  #unlike in list this numpy array sliced through in pointing towards same memory location its not copying if we really wanna copy we have to use copy()method

idx=np.argwhere(test_array==12)[0][0]
print(idx)

c2= np.round(np.random.rand(3,5)*10)
print(c2)

print(c2[0,2])
print(c2[0][2])
