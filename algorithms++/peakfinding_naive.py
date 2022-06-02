
# find a peak in 1D array - naive (linear search) approach
def find_peak(arr, peak):
    peak = 0
    if len(arr) == 0:
        return -1
    for i in range(len(arr)):
        if arr[i] >= peak:
            peak = arr[i]
            return peak
    return -1

