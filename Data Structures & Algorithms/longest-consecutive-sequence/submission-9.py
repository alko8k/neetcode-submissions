class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        length = 1

        nums = sorted(nums)

        temp = 1

        if not nums:
            return 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                continue
            elif nums[i + 1] == (nums[i] + 1) :
                temp += 1
            else:
                temp = 1
            length = max(temp, length)
        return length
            