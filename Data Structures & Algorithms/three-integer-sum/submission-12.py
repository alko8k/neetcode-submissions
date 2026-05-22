class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        threesums = []
        for i in range(len(nums) - 1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            s = i + 1
            l = len(nums) - 1
            while s < l:
                if nums[i] + nums[s] + nums[l] == 0:
                    threesums.append([nums[i], nums[s], nums[l]])
                    s += 1
                    l -= 1
                    while s < l and nums[s] == nums[s-1]:
                        s += 1
                    while s < l and nums[l] == nums[l+1]:
                        l -= 1
                elif nums[i] + nums[s] + nums[l] > 0: 
                    l -= 1
                else:
                    s += 1
        return threesums