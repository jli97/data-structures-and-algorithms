''' Container with Most Water '''

def maxArea(height):
    max_area = 0
    
    left = 0                    #Two pointers, one starts at 0, other starts at end
    right = len(height) - 1
    
    while (left < right):
        if(height[left] < height[right]): 
            max_area = max(max_area, height[left]*(right-left))
            left = left + 1
        
        else:
            max_area = max(max_area, height[right]*(right-left))
            right = right - 1
    
    return max_area

def main():
    height = [1,8,6,2,5,4,8,3,7]
    print("Result of maxArea():  " + str(maxArea(height)))

if __name__ == "__main__":
    main()
