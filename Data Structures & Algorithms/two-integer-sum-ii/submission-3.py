class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if target - numbers[i] == numbers[j]:
                    first = i + 1
                    second = j + 1
        return [first,second]