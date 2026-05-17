class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        last = range(len(nums))
        returned = list()
        for i in range(len(nums)):
            toAdd = 1
            for j in range(len(nums)):
                if i != j:
                    toAdd = toAdd * nums[j]
            returned.append(toAdd)
        return returned