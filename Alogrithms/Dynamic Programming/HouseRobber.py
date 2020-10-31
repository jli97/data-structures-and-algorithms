'''TOP DOWN/ MEMOIZATION'''

def robbery(nums, i, cache):
    if i >= len(nums): #No more houses left 
        return 0
    
    if cache[i] == -1: #Have not been traversed yet
        rob = nums[i] + robbery(nums, i + 2, cache) # If rob, skip next house
        skip = robbery(nums, i + 1, cache) #If skip, go to next house
        
        cache[i] = max(rob, skip) #The optimal deicion is the max of rob or skip
    
    
    return cache[i]
    

nums = [2,7,9,3,1]

cache = [-1] * len(nums)
print(robbery(nums, 0, cache))
