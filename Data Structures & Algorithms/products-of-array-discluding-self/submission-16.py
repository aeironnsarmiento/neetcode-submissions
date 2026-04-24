class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        product = 1
        zero = 0

        for num in nums:
            if num == 0:
                zero += 1
                continue
            product *= num

        for num in nums:
            if zero > 1:
                res.append(0)
            elif zero == 1:
                if num == 0:
                    res.append(product)
                else:
                    res.append(0)
            else:
                res.append(product // num)

        return res