import numpy as np
result=np.random.permutation(np.arange(10))
print(result)

a=np.random.rand(1000);
print(a)

import matplotlib.pyplot as plt
plt.hist(a, bins=100)
# plt.show()


b=np.random.rand(100000)
plt.hist(b,bins=200)

# plt.show()

c=np.random.rand(2,3)
print(c)