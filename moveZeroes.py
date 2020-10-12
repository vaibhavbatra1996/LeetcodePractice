"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
"""
class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        write = 0
        
        for read in range(1,len(nums)):
            if nums[write] == 0: 
                if nums[read] != 0:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
            else:
                write += 1

sol = Solution()
ip = [0,1,0,3,12]
sol.moveZeroes(ip)
print(ip)