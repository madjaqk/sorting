from time import time
from random import randint

start = time()

def selection(arr):
    print(arr)
    lowerbound, upperbound = 0, len(arr)-1
    while lowerbound < upperbound:
        cur_min_index, cur_max_index = lowerbound, upperbound
        for i in range(lowerbound,upperbound+1):
            if arr[i] < arr[cur_min_index]: cur_min_index = i
            elif arr[i] > arr[cur_max_index]: cur_max_index = i
        
        arr[lowerbound],arr[cur_min_index] = arr[cur_min_index],arr[lowerbound]
        
        if cur_max_index == lowerbound: cur_max_index=cur_min_index # Handles the case where the highest number had been in the lowest slot
        
        arr[upperbound],arr[cur_max_index] = arr[cur_max_index],arr[upperbound]
        lowerbound += 1
        upperbound -= 1
      
randomlist = [randint(0,10000) for x in range(100)]
selection(randomlist)
aftersort = sorted(randomlist)

if randomlist != aftersort:
    print("The sort didn't work!") # Sanity check
    for a in range(len(randomlist)):
        if randomlist[a] != aftersort[a]: print(a,randomlist[a],aftersort[a])


print(randomlist)


print("All done in {} seconds!".format(time()-start))

