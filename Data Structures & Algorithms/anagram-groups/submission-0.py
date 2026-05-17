class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        maps = dict()
        for string in strs:
            if maps.get(tuple(sorted(string))) != None:
                maps.get(tuple(sorted(string))).append(string)
            else:
                maps[tuple(sorted(string))] = [string]
        return list(maps.values())

