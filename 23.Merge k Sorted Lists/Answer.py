# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        # Helper function to merge two sorted linked lists
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy  

            # Traverse both lists until one is exhausted
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next  
                else:
                    cur.next = l2
                    l2 = l2.next  

                cur = cur.next  # Move the current pointer forward

            # Attach the remaining nodes (if any)
            if l1 is not None:
                cur.next = l1
            else:
                cur.next = l2

            # Return the head of the merged list (skip dummy)
            return dummy.next

        # Divide and conquer function
        def divide(lists, left, right):
            # Base case: only one list, return it directly
            if left == right:
                return lists[left]

            # Find the middle index
            mid = (left + right) // 2

            # Recursively divide the left half
            l1 = divide(lists, left, mid)
            l2 = divide(lists, mid + 1, right)

            # Merge the two halves
            return merge(l1, l2)

        # Start divide and conquer from the full range
        return divide(lists, 0, len(lists) - 1)