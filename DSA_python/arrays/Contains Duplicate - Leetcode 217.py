class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = set()
        for i in nums:
            if i not in l:
                l.add(i)
            else:
                return True
        return False