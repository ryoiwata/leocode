# Notes

To solve **LeetCode 872: Leaf-Similar Trees**, we need to determine if two binary trees have the same sequence of leaf values when read from left to right. A leaf is a node with no children, and the "leaf value sequence" is formed by these values in their natural order.

---

## 1. Problem Framing

* **Core Requirement**: Extract the leaf values from `root1` and `root2` in order and check if the resulting lists are identical.
* **Constraints**:
* The number of nodes in each tree is between  and .
* Node values range from  to .


* **Edge Cases**:
* **Single-node trees**: The leaf sequence is just that single node's value.
* **Different structures, same leaves**: Trees with completely different heights or shapes can still be leaf-similar.



---

## 2. Logic & Strategy: Depth-First Search (DFS)

The most efficient way to collect leaves in order is using a **pre-order DFS**.

1. **Traverse**: Traverse the tree recursively.
2. **Identify Leaves**: If a node has no `left` child AND no `right` child, it is a leaf. Add its value to a list.
3. **Compare**: Repeat this for both trees and compare the final sequences.

---

## 3. Complexity Analysis

* **Time Complexity**: , where  and  are the number of nodes in the two trees. We must visit every node to find all leaves.
* **Space Complexity**: , where  is the tree height (for the recursion stack) and  is the number of leaf nodes stored in our lists.

---

## 4. Full Solution (Debug Format)

```python
from collections import deque
from typing import Optional, List

# --- STEP 1: Define the structure ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

# Utility to build tree from LeetCode list format
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaves(node, leaves, tree_label):
            if not node:
                return
            
            # If it's a leaf, record it
            if not node.left and not node.right:
                print(f"    [{tree_label}] Found Leaf: {node.val}")
                leaves.append(node.val)
            
            # Continue searching Left then Right to maintain order
            get_leaves(node.left, leaves, tree_label)
            get_leaves(node.right, leaves, tree_label)

        print("--- Starting Leaf Extraction ---")
        leaves1, leaves2 = [], []
        
        print("\nProcessing Tree 1...")
        get_leaves(root1, leaves1, "Tree 1")
        
        print("\nProcessing Tree 2...")
        get_leaves(root2, leaves2, "Tree 2")
        
        print(f"\nSequence 1: {leaves1}")
        print(f"Sequence 2: {leaves2}")
        
        is_similar = leaves1 == leaves2
        print(f"Are they leaf-similar? {is_similar}")
        
        return is_similar

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # Example 1 from image
    t1_input = [3,5,1,6,2,9,8,None,None,7,4]
    t2_input = [3,5,1,6,7,4,2,None,None,None,None,None,None,9,8]
    
    root1 = build_tree(t1_input)
    root2 = build_tree(t2_input)
    
    sol = Solution()
    result = sol.leafSimilar(root1, root2)
    print(f"\nFinal Output: {result}")

```

Would you like to see how to solve this using a **Generator** in Python to save space by comparing leaves one by one as they are found?

# List as input

Yes, it is! This is a fundamental behavior in Python regarding **mutable objects** (like lists) being passed as arguments.

### How it works in your code:

1. **Object Reference:** When you pass `leaves1` or `leaves2` into `get_leaves`, you aren't passing a "copy" of the list; you are passing a **reference** to the exact same list object in memory.
2. **Shared Memory:** Because all recursive calls receive the same reference, any call that executes `leaves.append(node.val)` is modifying the single original list created in the main part of the `leafSimilar` function.
3. **Persistence:** This is why, after the recursion completely finishes and the "stack" collapses, the list in your main function is fully populated with all the leaf values found during the traversal.

---

### Visualizing the Modification

Imagine the list as a physical bucket. You pass that same bucket down to every "worker" (recursive function call). Whenever a worker finds a leaf, they drop a value into that specific bucket.

### Why this is standard for Trees:

* **Efficiency:** It avoids creating thousands of tiny lists and merging them as you return from recursion.
* **Simplicity:** The code doesn't need to "return" the list; it just acts on it.

### A Quick Warning (Mutable Defaults)

While passing a list as an **argument** is perfectly fine, you should never use an empty list as a **default parameter** value (e.g., `def get_leaves(node, leaves=[])`). In that case, Python would reuse the *exact same list* every time you called the function for the rest of your program's execution, leading to "ghost" data from previous runs appearing in new ones.

Would you like me to show you how you would rewrite this using **list concatenation** (returning a list instead of modifying one) so you can see the difference in style?