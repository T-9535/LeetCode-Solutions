# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val<list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
        
        i = m-1
        j = n-1
        k = m+n-1
        while j>0:
            if i>=0 and list1[i]>list2[j]:
                list1[k] = list1[i]
                i = i-1
                k = k-1
            else:

                list1[k] = list[j]
                j = j-1
                k = k-1

        