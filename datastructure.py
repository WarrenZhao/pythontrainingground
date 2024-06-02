# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedListFromList(object):
    def __init__(self, ori_list=[]):
        self.linkedlist = self.build_linkedlist(ori_list)
    
    
    def build_linkedlist(self, ori_list):
        if ori_list is None and len(ori_list) == 0:
            return None
        linked_list = cur = ListNode()
        for index, item in enumerate(ori_list):
            cur.next = ListNode(item, None)
            cur = cur.next
        return linked_list.next

