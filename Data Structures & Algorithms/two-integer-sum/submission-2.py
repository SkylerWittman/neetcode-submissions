class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        seen = {} # val : index

        for i, num in enumerate(nums):
            comp = target - num

            if comp in seen:
                return [seen[comp], i]
            
            seen[num] = i