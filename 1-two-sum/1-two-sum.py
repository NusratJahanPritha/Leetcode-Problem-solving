class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map=dict()
        for i in range(len(nums)):
            num=nums[i]
            complement=target-num
            if num in map:
                return [map[num],i]
            else:
                map[complement]=i