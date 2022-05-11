import numpy as np

a =np.array(1,6,-4,-2,-4)
min = 0
i = 0
for i in range(len(a)-1):
    if(a[i] < a[i+1]):
        min = a[i]

a.pop(i)
a-min
print(a)