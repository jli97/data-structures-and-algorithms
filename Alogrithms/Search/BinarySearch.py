sorted_arr = [1,2,3,4,5,6,7,8]
sorted_rotated_arr = [4,5,6,7,8,0,1,2]

''' Regular Binary Search of Sorted Array '''

def regularBinarySearch(target):
    left = 0
    right = len(sorted_arr) - 1

    while (left <= right): # Notice equality as we dont want the loop to break when 
                           # left == right which is the last possible iteration
        mid = left + (right - left) // 2

        if sorted_arr[mid] is target:
            return mid
        
        if sorted_arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    
    return -1 #If not found

''' Binary Search for lowest value in Rotated Array''' #returns idx of lowest value

def recursiveBinarySearch(arr, left, right, target):
    if right >= left:
        mid = left + (right - left) // 2
    
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return recursiveBinarySearch(arr, left, mid - 1, target)
        else:
            return recursiveBinarySearch(arr, mid + 1, right, target)
    else:
        return -1

def minValBinarySearch(): 
    left = 0
    right = len(sorted_rotated_arr) - 1

    while(left < right): #Notice no equality sign as when this breaks, left will be at the min value idx
        mid = left + (right - left) // 2

        if sorted_rotated_arr[mid] > sorted_rotated_arr[right]:
            left = mid + 1
        else:
            right = mid

    return left


def main():
    target  = 8

    print("Result of regularBinarySearch(): " + str(regularBinarySearch(target)))
    print("Result of regularBinarySearch(): " + str(minValBinarySearch()))


if __name__ == "__main__":
    main()
