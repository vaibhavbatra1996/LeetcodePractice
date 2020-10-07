"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

 

Example 1:

Input: s = "()"
Output: true

"""
class Solution:
    def isValid(self, s: str) -> bool:
        start = ['(','{','[']
        end = [')','}',']']
        temp = []
        for c in s:
            if c in start:
                temp.insert(0,c)
            if c in end:
                index = end.index(c)
                if temp[0] != start[index]:
                    return False
                else:
                    temp.remove(start[index])
        
        if temp == []:
            return True
        else:
            return False

sol = Solution()
print(sol.isValid('()'))