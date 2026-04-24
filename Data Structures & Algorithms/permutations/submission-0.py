class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(idx: int):
            # Base Case: We've swapped all the way to the end
            if idx == len(nums):
                res.append(nums[:])
                return
            
            # Recursive Step: Try swapping the current index with every number after it
            for i in range(idx, len(nums)):
                # 1. DO: Swap
                nums[idx], nums[i] = nums[i], nums[idx]
                # 2. RECURSE: Move to the next index
                backtrack(idx + 1)
                # 3. UNDO: Swap back to restore the original array state
                nums[idx], nums[i] = nums[i], nums[idx]

        backtrack(0)        
        return res