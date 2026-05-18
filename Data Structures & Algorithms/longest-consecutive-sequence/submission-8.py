class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        count = 1
        prev = None
        longest = 0
        if sortedNums == []:
            return 0
        for i in range(len(sortedNums) - 1):
            prev = sortedNums[i]
            if prev == sortedNums[i+1]:
                continue
            elif prev == sortedNums[i+1]-1:
                count+=1
            else :
                longest = max(count, longest)
                count = 1
        return max(longest,count)
        