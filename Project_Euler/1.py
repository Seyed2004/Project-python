# If we list all the natural numbers below 10 that are 
# multiples of 3 or 5 we get 3, 5, 6 and 9 The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000

import numpy as np
list=[]

for i in range(1,1000):
    if i % 3 ==0:
        list.append(i)

    elif i % 5 ==0:
        list.append(i)

    i +=1

print(list)
sum_list= sum(list)
print(sum_list)
