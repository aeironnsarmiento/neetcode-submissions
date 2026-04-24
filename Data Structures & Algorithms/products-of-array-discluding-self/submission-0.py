class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        product = 1
        zeroProduct = 0

        for num in nums:
            if num != 0:
                product *= num
            else:
                zeroProduct += 1

        for num in nums:
            if zeroProduct > 1:
                ans.append(0)
            elif zeroProduct == 1:
                if num == 0:
                    ans.append(product)
                else:
                    ans.append(0)
            else:
                ans.append(product // num)

        return ans