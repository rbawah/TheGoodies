
# find a peak in 1D array - naive (linear search) approach
def find_peak(arr):
    peak = 0
    if len(arr) == 0:
        return -1
    for i in range(len(arr)-1):
        if arr[i] >= peak:
            peak = arr[i]
    return peak
   

arr = [ 1, 3, 20, 4, 1, 0 ]
print("The peak point is", find_peak(arr))


if __name__ == '__main__':
    import timeit
    find_peak([ 1, 3, 20, 4, 1, 0 ])
    #findPeak([ 1, 3, 20, 4, 1, 0 ], len([ 1, 3, 20, 4, 1, 0 ]))
    print(timeit.timeit("find_peak([ 1, 3, 20, 4, 1, 0 ])", setup="from __main__ import find_peak"))
    #print(timeit.timeit("findPeak([ 1, 3, 20, 4, 1, 0 ], len([ 1, 3, 20, 4, 1, 0 ]))", setup="from __main__ import findPeak"))