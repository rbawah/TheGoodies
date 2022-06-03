
# Find a peak in 1D array - binary search (divide & conquer)

def findpeak_binary(arr):
    peak = None
    if len(arr) == 0:
        return None
    first = 0
    last = len(arr) - 1
    while last > first:
        midpoint = (first + last)//2
        print(last)
        if arr[midpoint] >= arr[midpoint - 1] and arr[midpoint] >= arr[midpoint + 1]:
            peak = arr[midpoint]
            return peak
        elif arr[midpoint] < arr[midpoint - 1]:
            last = midpoint - 1
        else:
            first = midpoint + 1
    return peak


arr = [ 1, 3, 20, 4, 1, 0 ]
print("The peak point is", findpeak_binary(arr))