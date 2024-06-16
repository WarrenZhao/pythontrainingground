import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not collections.Counter(magazine) - collections.Counter(ransomNote)

    def canConstruct_selfcode(self, ransomNote: str, magazine: str) -> bool:
        ch_dict = dict()
        for ch in magazine:
            if ch in ch_dict:
                ch_dict[ch] += 1
            else:
                ch_dict[ch] = 1
        for ch in ransomNote:
            if ch not in ch_dict:
                return False
            else:
                ch_dict[ch] -= 1
                if ch_dict[ch] == -1:
                    return False
        return True
        
s=Solution()
print(s.canConstruct("aab", "aab"))
                