class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * (len(nums) * 2)
        n = len(nums)

        for i, val in enumerate(nums):
            ans[i] = val
            ans[i + n] = val

        return ans