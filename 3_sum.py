三数之和

**思路：**这是知乎职人介绍所上，两位大牛手写的算法题。我的思路是先排序，然后两个 for 循环加二分查找，时间复杂度为O(pow(N, 2)*logN)，但还是没通过，有时间限制。后来结合 2Sum，想到不用两个 for 循环，直接用一个 for 循环，加二分查找。

第一种方法：

	class Solution(object):
	    def threeSum(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: List[List[int]]
	        """
	        def binary_search_right(nums, target):
	            if not nums:
	                return -1
	        
	            low = 0
	            high = len(nums)-1
	            res = -1
	            while low <= high:
	                middle = (low + high)/2
	                if nums[middle] == target:
	                    res = middle
	        
	                if nums[middle] > target:
	                    high = middle - 1
	                else:
	                    low = middle + 1
	            return res
	
	        nums.sort()
	        res = []
	        for i in range(len(nums) - 1):
	            if (i > 0) and (nums[i] == nums[i - 1]):
	                continue
	            for j in range(i + 1, len(nums)):
	                if (j > i + 1) and (nums[j] == nums[j - 1]):
	                    continue
	                x, y = nums[i], nums[j]
	                target = 0 - x - y
	                index = binary_search_right(nums[j+1:], target)
	                if (index != -1):
	                    res.append([x, y, 0 - x - y])
	        return res
	
第二种方法：

	class Solution(object):
	    def threeSum(self, nums):
	        """
	        :type nums: List[int]
	        :rtype: List[List[int]]
	        """
	        if len(nums) <= 2:
	            return []
	
	        def two_sum(nums, target):
	            low = 0
	            high = len(nums) - 1
	            res = []
	            while low < high:
	                if (low > 0) and (nums[low] == nums[low-1]):
	                    low += 1
	                    continue
	                if (high<len(nums)-1) and (nums[high]==nums[high+1]):
	                    high -= 1
	                    continue
	                if low >= high:
	                    return res
	                sum = nums[low] + nums[high]
	                if sum == target:
	                    res.append([nums[low], nums[high]])
	                    low += 1
	                    high -= 1
	                elif sum < target:
	                    low += 1
	                else:
	                    high -= 1
	            return res
	
	
	        nums.sort()
	        res = []
	        for i in range(len(nums) - 1):
	            if (i > 0) and (nums[i] == nums[i - 1]):
	                continue
	            temp = two_sum(nums[i+1:], -nums[i])
	            if temp:
	                for t in temp:
	                    t.append(nums[i])
	                    res.append(t)
	        return res

                
                
                
            
        
        

	                
	                
	                
	            
	        
	        
	        