class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        """
        一行python搞定
        """
        return len(s.strip().split(" ")[-1])
    def lengthOfLastWord_multi(self, s: str) -> int:
        items = s.split(" ")
        for item in reversed(items):
            if item.strip()=="":
                continue
            return len(item)
        return 0


