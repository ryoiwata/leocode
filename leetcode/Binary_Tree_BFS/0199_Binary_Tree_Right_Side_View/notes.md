To solve **LeetCode 199: Binary Tree Right Side View**, you need to return a list of values representing the nodes you would see if you were standing on the **right side** of the tree, looking at it from top to bottom.

---

### 1. Logic and Strategy: Level Order Traversal (BFS)

The most intuitive way to solve this is using a **Breadth-First Search (BFS)** with a queue. In a BFS, we visit the tree level by level.

**The Process:**

1. **Level by Level**: Traverse the tree one level at a time.
2. **Identify the Rightmost**: For each level, the **last node** you process is the one visible from the right side.
3. **Collect**: Add the value of that last node from each level to your result list.

---

### 2. Complexity Analysis

* **Time Complexity**: , where  is the number of nodes in the tree. We must visit every node to ensure we've found the rightmost one for every level.
* **Space Complexity**: , where  is the diameter of the tree. This is the maximum number of nodes stored in the queue at any given time (the width of the tree).

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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        print(f"--- Starting Binary Tree Right Side View ---")
        if not root:
            print("Tree is empty.")
            return []
        
        result = []
        queue = deque([root])
        level = 0
        
        while queue:
            level += 1
            level_length = len(queue)
            print(f"\nProcessing Level {level} (Nodes at this depth: {level_length})")
            
            for i in range(level_length):
                node = queue.popleft()
                
                # If this is the last node in the current level's queue,
                # it is the rightmost node visible from the side.
                if i == level_length - 1:
                    print(f"  Found Rightmost Node: {node.val}")
                    result.append(node.val)
                
                # Add children to queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            print(f"  Current View: {result}")

        print(f"\n--- Process Finished ---")
        print(f"Final Result: {result}")
        return result

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: root = [1,2,3,null,5,null,4]
    # Expected Output: [1, 3, 4]
    input_list = [1, 2, 3, None, 5, None, 4]
    tree_root = build_tree(input_list)
    sol.rightSideView(tree_root)

```

### Insight on Example 2

Looking at **Example 2** ():

* **Level 1**: Node `1` is visible.
* **Level 2**: Node `3` is visible (it is to the right of `2`).
* **Level 3**: Node `4` is visible.
* **Level 4**: Node `5` is visible.
* **Result**: `[1, 3, 4, 5]`. Even if a node is on the "left" branch of the tree, it can still be visible from the right if no nodes exist to its right at that specific depth.

Would you like to see how to solve this using a **Recursive DFS** approach instead of a queue?