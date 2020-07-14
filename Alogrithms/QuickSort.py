def quickSort(arr, low, high):
    if (low >= high):                   # Base case
        return
    else:
        i = partition(arr, low, high)   # i will be the index where the pivot is placed
        quickSort(arr, low, i - 1)      # recursive call on the left of i
        quickSort(arr, i + 1, high)     # recursive call on the right of i

def partition(arr, low, high):          # paritions arr and returns the index of where pivot should be 
    pivot = arr[high]                   # Can also pick median of three random elements or any other random element 
    wall = low - 1                      # Imagine this as a wall that divides the elements at the end of the partition, so it starts at low - 1

    for i in range(low, high):
        if arr[i] < pivot:              # when an element is smaller than the pivot, we want to move that element behind the wall
            wall = wall + 1             # this is done by moving the wall up one to make space and swapping the element that the wall is at currently with the smaller element 
            if i != wall:               
                temp = arr[i]
                arr[i] = arr[wall]
                arr[wall] = temp
    
    if wall + 1 != high:                # At this point, the wall should be in the correct position (all elements to the left < pivot, all elements to the right > pivot)
        temp = arr[wall + 1]            # so place the pivot in the correct position and return its index
        arr[wall + 1] = arr[high]
        arr[high] = temp

    return wall + 1                     # This is required to allow us to properly divide the array for the next recursive call

def main():
    arr = [5,4,3,2,1]

    quickSort(arr, 0, len(arr) - 1)

    print(arr)

if __name__ == "__main__":
    main()
