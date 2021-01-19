"""
804. Unique Morse Code Words
"""

ALPHABET = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",
            ".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
BASE = ord('a')

class Solution:
    def uniqueMorseRepresentations(self, words):
        global ALPHABET, BASE
        result = []
        for item in words:
            result.append(''.join([ALPHABET[ord(letter) - BASE] for letter in item]))
        return len(set(result))



s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
