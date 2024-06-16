from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        双指针写法，思路清晰
        由于可以不考虑val的元素，因此只要把nums前面的元素都改成非val即可。双指针的思路一定要牢记！
        """
        fast, slow = 0, 0
        while(fast < len(nums)):
            if nums[fast]==val:
                fast += 1
            else:
                nums[slow] = nums[fast]
                slow += 1
                fast += 1
        return slow
    def removeElement_turn(self, nums: List[int], val: int) -> int:
        re_index = len(nums)-1
        for index, item in enumerate(nums):
            while nums[re_index]==val:
                re_index -= 1
                if re_index==-1:
                    return 0
            if index >= re_index:  # 停止条件
                break
            if item==val:
                nums[index], nums[re_index] = nums[re_index], nums[index]
                re_index -= 1
        return re_index+1, nums
    
s = Solution()
print(s.removeElement([1], 1))
