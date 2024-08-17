from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for char in i:
                count[ord(char) - ord('a')] += 1
            anagrams[tuple(count)].append(i)
        
        return anagrams.values()