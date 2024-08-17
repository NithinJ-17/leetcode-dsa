class Solution:
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1
        while L < R :
            M = (L+R) // 2
            if nums[M] > nums[R]:
                L = M + 1
            else:
                R = M
        return nums[L]
            
