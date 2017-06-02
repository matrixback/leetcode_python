class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            if target - value in dict:
                return [dict[target-value], index]
            dict[value] = index