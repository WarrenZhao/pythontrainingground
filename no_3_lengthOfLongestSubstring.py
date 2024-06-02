class Solution(object):
    def lengthOfLongestSubstringSlideWindow(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        occ = set()
        rk = ans = 0
        for i in range(n):
            if i != 0:
                occ.remove(s[i-1])
            while rk < n and s[rk] not in occ:
                occ.add(s[rk])
                rk += 1
            ans = max(ans, rk-i)
        return ans
            

    def lengthOfLongestSubstringBruteForce(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_length = cur_length = 0
        for index in range(len(s)):
            substring = set()
            substring.add(s[index])
            cur_length = 1
            for sub_index in range(index + 1, len(s)):
                if s[sub_index] in substring:
                    max_length = max(cur_length, max_length)
                    cur_length = 1
                    break
                else:
                    substring.add(s[sub_index])
                    cur_length += 1
                max_length = max(max_length, cur_length)
        return max(max_length, cur_length)


print(Solution().lengthOfLongestSubstringSlideWindow("dvdf"))
