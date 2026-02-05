To solve **LeetCode 206: Reverse Linked List**, you need to change the direction of the pointers in a singly linked list so that the head becomes the tail and the tail becomes the head.

### 1. Logic and Strategy: Iterative Approach

The most efficient way to reverse a list in-place is using an iterative approach with three pointers: `prev`, `curr`, and `next`.

**The Process:**

1. **Initialize**: Set `prev` to `None` and `curr` to the `head` of the list.
2. **Iterate**: While `curr` is not `None`:
* **Save Next**: Store the next node (`curr.next`) in a temporary variable so you don't lose the rest of the list.
* **Reverse Link**: Point the current node's `next` back to `prev` (`curr.next = prev`).
* **Move Forward**: Shift both `prev` and `curr` one step forward.


3. **Return**: Once the loop ends, `prev` will be pointing to the new head.

---

### 2. Complexity Analysis

* **Time Complexity**: , where  is the number of nodes in the list. We visit each node exactly once.
* **Space Complexity**: . We only use a few pointer variables regardless of list size.

---

### 3. Full Solution (Debug Format)

```python
from typing import Optional

# --- STEP 1: Define the structure ---
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    # Formats print output to show the list sequence
    def __repr__(self):
        nodes = []
        curr = self
        while curr:
            nodes.append(str(curr.val))
            curr = curr.next
        return " -> ".join(nodes)

def build_linked_list(values):
    if not values: return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# --- STEP 2: Your Algorithm (Iterative) ---
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        print(f"--- Starting Reverse Linked List ---")
        if not head:
            print("List is empty.")
            return None
        
        print(f"Original list: {head}")
        
        prev = None
        curr = head
        count = 0
        
        while curr:
            count += 1
            print(f"\n[Step {count}] Processing Node: {curr.val}")
            
            # Temporary storage of the next node
            next_node = curr.next
            print(f"  Next node saved: {next_node.val if next_node else 'None'}")
            
            # Reverse the pointer
            curr.next = prev
            print(f"  Link reversed: {curr.val} -> {prev.val if prev else 'None'}")
            
            # Move pointers forward
            prev = curr
            curr = next_node
            
            print(f"  Pointers moved forward. Current 'prev' is now: {prev.val}")

        print(f"\n--- Process Finished ---")
        print(f"Final Reversed List: {prev}")
        return prev

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: head = [1,2,3,4,5]
    example_input = [1, 2, 3, 4, 5]
    head = build_linked_list(example_input)
    sol.reverseList(head)

```

### Follow-up: Recursive Approach

As mentioned in the constraints, you can also solve this recursively. The recursive logic works by reaching the end of the list and then reversing the pointers as the function calls return (the "unwinding" of the stack).

Would you like me to rewrite the solution using the **Recursive** method so you can compare the two?