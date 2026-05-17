class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = dict()
        returned = list()
        for num in nums:
                counts[num] = counts.get(num, 0) + 1
        sortedCounts = sorted(counts.items(), key=lambda x: x[1], reverse = True)

        i = 0
        while k > 0:
            returned.append(sortedCounts[i][0])
            i += 1
            k -= 1
        return returned
