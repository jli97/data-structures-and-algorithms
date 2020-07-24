''' Container with Most Water '''

def maxArea(self, height):
    """
    :type height: List[int]
    :rtype: int
    """
    
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