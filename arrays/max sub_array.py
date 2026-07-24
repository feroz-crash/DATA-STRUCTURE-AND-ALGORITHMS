from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n=len(nums)
        max1=float('-inf')
        sm=0
        for i in range(n):
            sm+=nums[i]
            if sm>max1:
                max1=sm
            if sm<0:
                sm=0
            
        return max1
nums = [-2,1,-3,4,-1,2,1,-5,4]
sol = Solution()
print(sol.maxSubArray(nums))  # Output: 6