from time import time
from random import randint

start = time()

def insertion(arr):
    print(arr)
    for i in range(1,len(arr)):
        j=i
        while arr[j]<arr[j-1] and j>0:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            j-=1

"""
The while loop implements a form of bubble sort, which I suspect means that this code isn't as efficient as it should be.  I'm not sure how to do insertions in Python, though.
"""
    
randomlist = [randint(0,10000) for x in range(100)]
insertion(randomlist)
aftersort = sorted(randomlist)

if randomlist != aftersort:
    print("The sort didn't work!") # Sanity check
    for a in range(len(randomlist)):
        if randomlist[a] != aftersort[a]: print(a,randomlist[a],aftersort[a])


print(randomlist)


print("All done in {} seconds!".format(time()-start))

