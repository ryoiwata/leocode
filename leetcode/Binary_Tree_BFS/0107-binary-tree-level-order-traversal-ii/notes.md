leetcode.com/problems/binary-tree-level-order-traversal-ii/

This is a classic variation of the Breadth-First Search (BFS) pattern. Let’s break it down so you can nail this in an interview setting.

---

## 1. Problem Framing

The goal is to perform a **Level Order Traversal**, but instead of returning levels from top-to-bottom, we return them from **bottom-to-top**.

* **Core Requirement:** Group nodes by their depth, but order the final list such that the leaf-level lists come first.
* **Constraints:**
* The number of nodes can range from 0 to 2000.
* Node values are between -1000 and 1000.


* **Edge Cases:**
* **Empty Tree (`root = None`):** Should return an empty list `[]`.
* **Single Node:** Should return `[[val]]`.
* **Skewed Tree:** Ensure the logic handles deep, narrow trees (like a linked list) just as well as balanced ones.



---

## 2. Logic & Strategy

The most efficient approach is **Breadth-First Search (BFS)** using a **Queue**.

1. **Standard BFS:** We use a queue to traverse the tree level by level. For each level, we record the number of nodes currently in the queue, process them all, and add their children to the queue for the next level.
2. **Level Storage:** As we finish processing each level, we append that level's list of values to a master result list.
3. **The "Bottom-Up" Twist:** * **Option A:** Perform a standard top-down BFS and then **reverse** the final list at the end.
* **Option B:** Use a **double-ended queue (deque)** for the result list and `appendleft()` each new level.
* *Note:* Reversing a list of length  (height) is , which is negligible compared to the  traversal.



---

## 3. Complexity Analysis

Let  be the number of nodes in the tree.

* **Time Complexity: **
* We visit every node exactly once. Each node is added to and removed from the queue exactly once.


* **Space Complexity: **
* In the worst case (a perfect binary tree), the queue will hold the entire bottom level, which contains roughly  nodes. The output list also stores  values.



---

## 4. Full Solution

```python
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level_values = []
            
            # Process all nodes at the current depth
            for _ in range(level_size):
                node = queue.popleft()
                current_level_values.append(node.val)
                
                # Add children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Append the current level's values to our result
            result.append(current_level_values)
            
        # Reverse the list to get bottom-up order
        return result[::-1]

```

Would you like me to explain how you might solve this using **Recursion (DFS)** instead, and why BFS is usually preferred for this specific problem?