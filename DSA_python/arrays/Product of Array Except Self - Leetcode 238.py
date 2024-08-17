class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        result = [1] * len(nums)
        for i in range(0,len(nums)):
            result[i] = p
            p *= nums[i]
        
        p = 1
        for i in range(len(nums)-1,0,-1):
            result[i]*=p
            p*=nums[i]
        result[0] = p
        return result