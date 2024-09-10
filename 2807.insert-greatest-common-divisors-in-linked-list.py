#
# @lc app=leetcode id=2807 lang=python3
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b!=0:
                a,b=b,a%b
            return a
        prev,curr=head,head.next
        while curr:
            temp = ListNode(gcd(prev.val,curr.val))
            temp.next = curr
            prev.next=temp
            prev=curr
            curr=curr.next
        return head
        
# @lc code=end

