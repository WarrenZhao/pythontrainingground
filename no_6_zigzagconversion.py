class Solution(object):
    def convert(self, s, numRows):
        """
        巧妙使用flag
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if numRows==1 or numRows>n:
            return s
        t = 2*numRows-2
        ans = [[] for _ in range(numRows)]
        flag = 1
        rowIndex = 0
        for _, item in enumerate(s):
            ans[rowIndex].append(item)
            rowIndex += flag
            if rowIndex==numRows-1 or rowIndex==0:
                flag = -flag
        return "".join("".join(ch) for ch in ans)


    def convert_di(self, s, numRows):
        """
        直接拼接字符串实现
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        t = 2* numRows-2
        ans = []
        if numRows==1 or numRows > n:
            return s
        else:
            for i in range(numRows):
                for j in range(0, n-i, t):  
                    # 这里的边界值设置为n-i是因为要满足条件，
                    # 如果i行只有第一个字母，那么i+j<n，
                    # 如果i行有第二个字母，那么j+t-i<n，
                    # 第二个字母的id显然是大于第一个字母的，因此满足更苛刻的条件（第一个）。
                    # 每行的第一个字母
                    ans.append(s[i+j])
                    # (非首位行的)每行的第二个字母
                    if 0 < i < numRows-1 and j+t-i < n:
                        ans.append(s[j+t-i])
        return "".join(ans)
                    

# 测试代码
t = Solution()
# t.convert("PAYPALISHIRING", 3)
print(t.convert("AB", 1))
