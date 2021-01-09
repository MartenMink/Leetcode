"""
1370. Increasing Decreasing String
"""

class Solution:
    def sortString(self, s):
        codes = {}
        result = []
        sortset = str(sorted(set(s)))
        for uitem in sortset:
            codes[uitem] = s.count(uitem)
        while sum(codes.values()) > 0:
            for item in sortset:
                if codes[item] > 0:
                    result.append(item)
                    codes[item] -= 1
            for item in sortset[::-1]:
                if codes[item] > 0:
                    result.append(item)
                    codes[item] -= 1
        return ''.join(result)


s = Solution()
print(s.sortString("spo"))
