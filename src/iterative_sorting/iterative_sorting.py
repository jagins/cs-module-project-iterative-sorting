# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for index in range(0, len(arr) - 1):
        smallest_index = index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        minIndex = index + 1 
        #start the loop at the minIndex and not at 0
        for minIndex in range(minIndex, len(arr)):
            #if the element in this loop is smaller than the element in outer loop swap the smallest_index to be min
            if arr[minIndex] < arr[smallest_index]:
                smallest_index = minIndex

        # TO-DO: swap
        # Your code here
        temp = arr[smallest_index]
        arr[smallest_index] = arr[index]
        arr[index] = temp
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    #start the loop at 1 to count for the length of the array and not the index
    for i in range(1, len(arr)):
        #compare the element in current index to the element in the next slot over
        for index in range(len(arr) - 1):
            #check to see if element at the current index is larger than the next elemenet, if it is trigger the bubble sort
            if arr[index] > arr[index + 1]:
                temp = arr[index]
                arr[index] = arr[index + 1]
                arr[index + 1 ] = temp

    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    # Your code here


    return arr
