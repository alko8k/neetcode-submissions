class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for n in nums:
            if n in freqMap:
                freqMap[n] += 1
            else:
                freqMap[n] = 1

        pairs = []
        for num in freqMap:
            pairs.append([freqMap[num], num])

        pairs.sort(reverse=True)

        result = []
        for i in range(k):
            result.append(pairs[i][1])
        return result


        

