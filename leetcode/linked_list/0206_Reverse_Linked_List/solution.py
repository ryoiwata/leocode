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