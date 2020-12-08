''' 
    Enumerate nums as intervals (start, end). Start at index 0 and find
    the maximum end of all indexes within the interval of index 0. Jump
    to the max index, and repeat the search for the farthest endpoint 
    within the new interval. 
'''

def jump(nums):
        
        intervals = [(i, i + nums[i]) for i in range(len(nums))]

        ans = 0
        j = 0 # Used to iterate over the other intervals interval[start] can jump to
        start, end = 0, 0
    
        while start < len(nums) - 1:
            ans += 1
            r = end # Temp var for max distance interval[start] can reach
                    
            # For every interval[start][0] can reach
            while j < len(nums) and intervals[j][0] <= r: 
                end = max(end, intervals[j][1]) # Pick the farthest reaching interval    
                j += 1
            
            start = end # Repeat process for new start index
        
        return ans

nums = [2,3,1,1,4]
print(jump(nums))
