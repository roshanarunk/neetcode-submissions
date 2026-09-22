class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = [[]]
        
        def subset(i):
            for x in list(sols):
                sols.append(x + [nums[i]])
        for x in range(len(nums)):
            subset(x)
        return sols