"""
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alphadict = {}
        for i in range(len(s)):
            if s[i] not in alphadict and t[i] not in alphadict.values():
                alphadict[s[i]] = t[i]
            else:
                if s[i] in alphadict:
                    if alphadict[s[i]] != t[i]:
                        return False
                else:
                    for k,v in alphadict.items():
                        if v == t[i] and k != s[i]:
                            return False
        return True

sol = Solution()
print(sol.isIsomorphic('ab','aa'))