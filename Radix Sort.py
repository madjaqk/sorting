from time import time
from random import randint
from math import log10, ceil

# Written in Python 3.4
# Right now, only works for positive integers

start = time()

def radix(arr):
    print(arr)
    highest=arr[0]
    for i in arr:
        if i>highest : highest=i
    numdigits=ceil(log10(highest+1)) # Searches for the highest value so the program can determine the maximum number of digits
    for count in range(0,numdigits): # Executes for each digit, starting with rightmost
        holder = [[] for _ in range(10)] # Fun fact: "[[]] * 10" will make this break in a baffling way!
        for val in arr:
            bucket = (val//(10**count))%10 # Calculate the digit in a given position...
            #print(val,bucket)
            holder[bucket].append(val) # ...and assign the value to one of ten buckets based on that.
        #print(holder)
        arr = []
        for bucketcount in range(10):
            arr.extend(holder[bucketcount]) # There's probably a faster way to concatenate lists, but I couldn't find one on Google.
    return(arr)


#radix([14,18,24,26,99,88,45])
    
randomlist = [randint(1,10001) for x in range(100)]
randomlist = radix(randomlist)
aftersort = sorted(randomlist)
"""
if randomlist != aftersort:
    print("The sort didn't work!") # Sanity check
    for a in range(len(randomlist)):
        if randomlist[a] != aftersort[a]: print(a,randomlist[a],aftersort[a])

"""
print(randomlist)


print("All done in {} seconds!".format(time()-start))

