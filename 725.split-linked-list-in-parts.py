#
# @lc app=leetcode id=725 lang=python3
#
# [725] Split Linked List in Parts
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
            length = 0
            temp=head
            while temp:
                length +=1
                temp=temp.next
            s=length//k
            r=length%k
            ans=[]
            prev=None
            temp=head
            while k>0:
                pointer=temp
                for i in range(s):
                    prev=temp
                    temp=temp.next
                if r>0:
                    prev=temp
                    temp=temp.next
                    r-=1
                if prev:
                    prev.next=None
                ans.append(pointer)
                k-=1
                
            return ans    
            
        
# @lc code=end

