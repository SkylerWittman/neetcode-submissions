class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2:
            return [0, 1]

        complement = {} # val : index

        for i, num in enumerate(nums):
            comp = target - num

            if num in complement:
                return [complement[num], i]
            
            complement[comp] = i