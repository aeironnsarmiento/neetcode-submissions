class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1 # normal setup
        res = nums[0]

        while l <= r: #normal setup
            if nums[l] < nums[r]: # just check if biggest in left bc that means its sorted properly
                res = min(res, nums[l])
                break
            m = l + (r - l) // 2 #normal setup
            if nums[l] <= nums[m]: #normal setup
                l = m + 1
            else: #normal setup
                r = m - 1
            res = min(res, nums[m]) # we want the min so we compare current res to the m pointer (m is the one looking)

        return res