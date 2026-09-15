class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = defaultdict(list)

        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord('a')] += 1
            grams[tuple(count)].append(x)
        return list(grams.values())
                