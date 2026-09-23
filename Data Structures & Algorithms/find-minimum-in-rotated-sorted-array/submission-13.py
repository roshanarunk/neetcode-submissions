class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1
        minVal = nums[0]
        while l <= r:
            mid = l + (r - l)//2
            if nums[r] >= nums[l]:
                minVal = min(nums[l], minVal)
                l = r+1
            else:
                if nums[mid] > nums[r]:
                    l = mid + 1
                    minVal = min(nums[r], minVal)
                else:
                    minVal = min(nums[mid], minVal)
                    r = mid - 1
        return minVal

