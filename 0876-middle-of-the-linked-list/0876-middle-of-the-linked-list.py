# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=head
        count=0
        while current:
            count+=1
            current=current.next
        # print(count)
        take=count//2
        if take==0:
            take=1
        if count%2==0:
            take=take+1
        previous=None
        current=head
        # print(take)
        make=0
        if count%2==0:
            make+=1
        while current:
            tem=current
            current=current.next
            if current==None:
                current=tem
            make+=1
            # print(take)
            if make==take:
                # print(current)
                return current
        # return None