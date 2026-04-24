class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = set()

        def dfs(i, cur, total):
            if total == target:
                res.add(tuple(cur))
                return
            if i >= len(nums) or total > target:
                return

            cur.append(nums[i])
            dfs(i + 1, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return [list(s) for s in res]