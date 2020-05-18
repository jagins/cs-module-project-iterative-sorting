def linear_search(arr, target):
    #start at arr[0] and compare to the next element
    for i in range(len(arr)):
         #if target matches arr[i]
        if target == arr[i]:
             return i
    return -1

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #step 1 left = 0 right = length - 1 (right how many index we have)
    left = 0
    right = len(arr) - 1
    #step 2 while loop through left <= right
    while left <= right:
        #step 3 find the midpoint of the array
        midpoint = left + (right - 1) // 2
        #step 4 compare target to arr[midpoint]
        if arr[midpoint] == target:
            #step 3 if it's a match return the index
            return midpoint
    #step 5 else if array[midpoint] < target move left
        elif arr[midpoint] < target:
            #left = mid + 1
            left = midpoint + 1
    #step 6 else move right
        else:
            #right = mid - 1
            right = midpoint - 1
    return -1  # not found
