"""
1704. Determine if String Halves Are Alike
"""

VOWELS = ['a', 'e', 'i', 'o', 'u']

class Solution:
    def halvesAreAlike(self, s):
        global VOWELS
        part1 = sum([True if item in VOWELS else False for item in s[:len(s)//2].lower()])
        part2 = sum([True if item in VOWELS else False for item in s[len(s)//2:].lower()])
        return part1 == part2

s = Solution()
print(s.halvesAreAlike("AbCdEfGh"))
