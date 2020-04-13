# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # Iterate through remaining elements in array
        for j in range(cur_index + 1, len(arr)):
            # Check if any other elements are smaller
            if arr[j] < arr[smallest_index]:
                # Assign new smallest element to smallest index
                smallest_index = j

        # swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]




    return arr


def bubble_sort( arr ):
    # loop through each element
    for i in range(len(arr)-1):
        # loop through remaining
        for j in range(len(arr)-i-1):
            # swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr