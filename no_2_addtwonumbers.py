from datastructure import LinkedListFromList, ListNode
from typing import Optional


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        cur = dummy = ListNode()
        while l1 or l2 or carry:
            carry = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry = carry // 10
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next



    def addTwoNumbersIteration(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        """
        这种方法是对原有函数进行了重载，然后通过增加一个进位carry参数来达到统一迭代代码的目的
        但是这种迭代的方法力扣官网没有执行通过，不知道是不是改变了方法参数的问题
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is None:
            return ListNode(carry) if carry==1 else None
        if l1 is None:
            l1, l2 = l2, l1
        carry += l1.val + l2.val if l2 else 0
        l1.val = carry % 10
        carry = carry // 10
        l1.next = self.addTwoNumbersIteration(l1.next, l2.next, carry)  # 在类内部迭代的时候，需要使用self才能调用
        return l1


# 测试用例验证代码
l1 = LinkedListFromList([2, 4, 3]).linkedlist
l2 = LinkedListFromList([5, 6, 4]).linkedlist

result = Solution().addTwoNumbers(l1=l1, l2=l2)
while result:
    print(result.val)
    result = result.next
