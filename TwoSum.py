class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            secondNum = target - nums[i]
            if secondNum in numDict:
                return [i,numDict[secondNum]]
            numDict[nums[i]] = i

sol = Solution()
print(sol.twoSum([3,3],6))