To solve **LeetCode 700: Search in a Binary Search Tree**, you take advantage of the specific properties of a Binary Search Tree (BST). In a BST, for any given node, all values in the **left subtree** are smaller than the node's value, and all values in the **right subtree** are larger.

---

### 1. Logic and Strategy: BST Traversal

Because the tree is ordered, you don't need to search every node. You can "discard" half of the remaining tree at each step.

**The Process:**

1. **Compare**: Look at the current node's value against the target `val`.
2. **Match**: If `node.val == val`, you've found it! Return the current node.
3. **Go Left**: If the target `val` is **smaller** than the current node's value, move to the left child.
4. **Go Right**: If the target `val` is **larger** than the current node's value, move to the right child.
5. **Not Found**: If you reach a `None` node, the value does not exist in the tree.

---

### 2. Complexity Analysis

* **Time Complexity**: , where  is the height of the tree. In a balanced BST, this is , but in the worst case (a skewed tree), it can be .
* **Space Complexity**:
* **Recursive**:  for the recursion stack.
* **Iterative**:  as we only use a single pointer to move down the tree.



---

### 3. Full Solution (Debug Format)

```python
from collections import deque
from typing import Optional, List

# --- STEP 1: Define the structure ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # Helper to visualize the subtree in the console
    def __repr__(self):
        result = []
        queue = deque([self])
        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("null")
        # Trim trailing nulls for cleaner output
        while result and result[-1] == "null":
            result.pop()
        return "[" + ",".join(result) + "]"

def build_tree(values):
    if not values: return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

# --- STEP 2: Your Algorithm ---
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        print(f"--- Starting Search in BST for value: {val} ---")
        curr = root
        
        while curr:
            print(f"Currently at Node: {curr.val}")
            
            if curr.val == val:
                print(f"  Target {val} FOUND!")
                return curr
            
            if val < curr.val:
                print(f"  {val} < {curr.val}: Moving LEFT")
                curr = curr.left
            else:
                print(f"  {val} > {curr.val}: Moving RIGHT")
                curr = curr.right
        
        print(f"  Node with value {val} not found in tree.")
        return None

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: root = [4,2,7,1,3], val = 2
    # Expected Output: [2,1,3]
    input_list = [4, 2, 7, 1, 3]
    target = 2
    tree_root = build_tree(input_list)
    result_node = sol.searchBST(tree_root, target)
    print(f"\nFinal Subtree: {result_node}")

```

Would you like me to show you how to perform an **Insert** operation on this BST while maintaining its sorted property?