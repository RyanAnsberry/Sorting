# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge( arrA, arrB ):
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    # TO-DO
    # Index iterators for each array
    i,j,k = 0,0,0
    
    # Compare and sort elements of both arrays to merged_arr
    while i < len( arrA ) and j < len( arrB ):
        if arrA[i] < arrB[j]:
            merged_arr[k] = arrA[i]
            k = k + 1
            i = i + 1
        else:
            merged_arr[k] = arrB[j]
            k = k + 1
            j = j + 1

    # Add any remaining elements to merged_arr
    while i < len( arrA ):
        merged_arr[k] = arrA[i]
        k = k + 1
        i = i + 1
    
    while j < len( arrB ):
        merged_arr[k] = arrB[j]
        k = k + 1
        j = j + 1       
    
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    # Base Case:
    if len( arr ) > 1:
        # Continuously divide until single item arrays (recursion)
        left = merge_sort( arr[ 0 : len( arr ) // 2 ])
        right = merge_sort( arr[ len( arr ) // 2 : ])

        # Compare values and sort into arrays
        arr = merge( left, right )

    return arr


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr
