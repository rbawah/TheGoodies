
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
# n = len(arr)
print("The peak point is", find_peak(arr))