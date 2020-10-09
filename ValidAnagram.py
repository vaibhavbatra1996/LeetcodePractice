"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

"""
import string
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alphabets = string.ascii_lowercase
        
        if len(s) != len(t):
            return False
        
        for i in alphabets:
            if i in s and i in t:
                if s.count(i) == t.count(i):
                    continue
                else:
                    return False
                
            if i in s and i not in t:
                return False
            
            if i in t and i not in s:
                return False
        
        return True

sol = Solution()
print(sol.isAnagram("anagram","nagaram"))