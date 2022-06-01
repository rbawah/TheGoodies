def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last)//2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = list[midpoint] - 1
    return None


def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target Not Found.")



nums = [1,2,3,4,5,6,7,8,9,10]

result = binary_search(nums, 1)
verify(result)
