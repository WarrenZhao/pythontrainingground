class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 大写字母转小写
        low_s = s.lower()
        # 排除所有的符号
        new_s = "".join(ch for ch in low_s if ch.isalnum())
        # 验证是否是回文
        return new_s==new_s[::-1]
