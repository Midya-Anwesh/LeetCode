# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# creat a method to compare between two listnode or nonetypes
def __lt__(self: Optional[ListNode], head: Optional[ListNode]):
    if self != None and head != None:
        return True if self.val < head.val else False
    if head is None:
        return True
    return False

# overload less than operator for listnode class
ListNode.__lt__ = __lt__

from heapq import heapify, heappush, heappop
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap, ret = [], None
        temp = None
        heapify(heap)
        # Add head of all linked lists in min-heap except null
        for head in filter(lambda h: not h is None, lists):
            heappush(heap, head)

        while len(heap):
            head = heappop(heap)
            # if head is None:
            #     continue
            if ret is None:
                ret = head
                temp = ret
            else:
                temp.next = head
                temp = temp.next
            head = head.next
            temp.next = None
            if not head is None:
                heappush(heap, head)
        
        return ret
