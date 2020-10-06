"""
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.

"""

import string
class Solution:
    def firstUniqChar(self, s: str) -> int:
        i = [s.index(c) for c in string.ascii_lowercase if s.count(c) == 1]
        return min(i) if i else -1

sol = Solution()
print(sol.firstUniqChar("abcab"))