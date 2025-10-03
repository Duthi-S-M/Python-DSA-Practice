class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        k = 1             
        prev = nums[0]    

        for i in nums[1:]:  
            if i != prev:   
                nums[k] = i 
                k += 1
                prev = i    

        return k
