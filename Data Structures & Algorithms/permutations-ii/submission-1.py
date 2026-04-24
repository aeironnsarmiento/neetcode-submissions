class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        
        def dfs(idx):
            if idx >= len(nums):
                res.add(tuple(nums[:]))
                return
            
            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        dfs(0)        
        return [list(s) for s in res]