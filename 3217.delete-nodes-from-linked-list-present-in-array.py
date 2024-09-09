#
# @lc app=leetcode id=3217 lang=python3
#
# [3217] Delete Nodes From Linked List Present in Array
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums=set(nums)
        temp=None
        prev=None
        while head is not None:
            if head.val in nums:
                head = head.next
                if prev is not None:
                    prev.next = head
                continue
            else:
                if temp==None:
                    temp=head
                prev=head
                head = head.next
        return temp
        
        
# @lc code=end

