from time import time
from random import randint

start = time()

def bubble(arr):
    done = False
    while not done:
        done = True
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1],arr[i] # In Python, this actually works!
                done = False

randomlist = [randint(0,10000) for x in range(100)]

bubble(randomlist)
print(randomlist)

print("All done in {} seconds!".format(time()-start))

