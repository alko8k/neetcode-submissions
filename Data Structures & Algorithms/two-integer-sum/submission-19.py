class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i, n in enumerate(nums):
            find = target - n
            if find in numMap:
                return [numMap[find], i]
            else:
                numMap[n] = i
        return
        

