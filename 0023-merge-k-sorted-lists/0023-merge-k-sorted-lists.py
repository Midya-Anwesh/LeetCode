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

        # ret is newly created linked list and heap is min-heap
        heap, ret = [], None

        # temp is to track the last node of newly created linked list
        temp = None
        heapify(heap)

        # Add head of all linked lists in min-heap except null
        for head in filter(lambda h: not h is None, lists):
            heappush(heap, head)

        # exhaust all heads of linked lists that are not null
        while len(heap):
            head = heappop(heap)
            # if head of linked list to be returned is null then assign it to head
            # and update the temp
            if ret is None:
                ret = head
                temp = ret
            # add head after the temp and update the position of temp
            else:
                temp.next = head
                temp = temp.next
            head = head.next
            temp.next = None
            # if there is a node adjecent to current head then add it to heap
            if not head is None:
                heappush(heap, head)
        # return the head of newly created linked list
        return ret
