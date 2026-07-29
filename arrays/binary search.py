from typing import List
class Solution:
    def binarysearch(self,nums: List[int],target: int) ->int:
        l,r=0,len(nums)-1
        while l<=r:
            mid=r+(l-r)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid-1
        return -1
if __name__ == "__main__":
    sol=Solution()
    print(sol.binarysearch([-1,0,3,5,9,12],9)) # Expected: 4
    print(sol.binarysearch([-1,0,3,5,9,12],2)) # Expected: -1