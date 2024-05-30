from typing import List

class Solution:

    # 暴力搜索，空间复杂度为O(1),只有一个临时变量，时间复杂度O(n^2)，时间复杂度很高
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if target == nums[i] + nums[j]:
                    return [i, j]
    

    # 使用哈希表法，空间复杂度为O(n),需要将所有的数据都存储在一个哈希表中，时间复杂度为O(n)，任意一个元素的查找时间复杂度为O(1)
    def twoSumHash(self, nums: List[int], target: int) -> List[int]:
        hashtable = dict()
        for index, value in enumerate(nums):
            if target - value in hashtable:
                return [index, hashtable[target - value]]
            else:
                hashtable[value] = index

    
    # 使用pythonic的方法，利用切片实现
    def twoSumSlice(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
        # 计算需要找到的下一个目标数字
            res = target-nums[i]
                # 遍历剩下的元素，查找是否存在该数字
            if res in nums[i+1:]:
                # 若存在，返回答案。这里由于是两数之和，可采用.index()方法
                # 获得目标元素在nums[i+1:]这个子数组中的索引后，还需加上i+1才是该元素在nums中的索引
                return [i, nums[i+1:].index(res)+i+1]



