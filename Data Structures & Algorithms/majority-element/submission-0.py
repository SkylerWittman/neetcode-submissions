class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # seen = defaultdict(int)
        # res = maxCount = 0

        # for num in nums:
        #     seen[num] += 1
        #     if maxCount < seen[num]:
        #         res = num
        #         maxCount = seen[num]
        # return res

        nums.sort()
        return nums[len(nums) // 2]