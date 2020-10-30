''' 
    Enumerate nums as intervals (start, end). Start at index 0 and find
    the maximum end of all indexes within the interval of index 0. Jump
    to the max index, and repeat the search for the farthest endpoint 
    within the new interval. 


'''

def jump(nums):
        
        intervals = [(i, i + nums[i]) for i in range(len(nums))]

        ans = 0
        j = 0
        start, end = 0, 0
    
        while start < len(nums) - 1:
            ans += 1
            r = end
            
            while j < len(nums) and intervals[j][0] <= r:
                end = max(end, intervals[j][1])
                j += 1
            
            start = end
        
        return ans

nums = [2,3,1,1,4]
print(jump(nums))
