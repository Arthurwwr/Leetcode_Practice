#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy #pointer to the node before pair


        while prev.next and prev.next.next:
            #identify two nodes to swap
            first = prev.next
            second = prev.next.next

            # swap first and second
            first.next = second.next
            second .next = first
            prev.next = second
            prev = first
        return dummy.next


# ===== Helper functions =====

# Convert list → linked list
def build_linked_list(arr):
    dummy = ListNode(0)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next


# Print linked list
def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    print(res)


# ===== Test =====

if __name__ == "__main__":
    arr = [1, 2, 3, 4]   # test input

    head = build_linked_list(arr)

    sol = Solution()
    new_head = sol.swapPairs(head)

    print_list(new_head)