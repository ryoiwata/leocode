To solve **LeetCode 104: Maximum Depth of Binary Tree**, we need to find the length of the longest path from the root node down to the farthest leaf node. This is a fundamental tree problem that can be solved elegantly using recursion or iteration.

---

## 1. Problem Framing

* **Core Requirement**: Return the maximum depth of the given binary tree.
* **Constraints**: The number of nodes is between  and , and node values range from  to .
* **Edge Cases**:
* **Empty Tree**: If `root` is `null`, the depth is .
* **Single Node**: The depth is .
* **Skewed Tree**: A tree where every node only has one child (resembling a linked list).



---

## 2. Logic & Strategy: Depth-First Search (DFS)

The most intuitive approach is a **Recursive DFS** (specifically, a post-order traversal).

1. **Base Case**: If the current node is `None`, its depth is .
2. **Recursive Step**:
* Find the maximum depth of the **left** subtree.
* Find the maximum depth of the **right** subtree.


3. **Result**: The depth of the current node is the maximum of those two subtrees, **plus 1** (to account for the current node itself).

---

## 3. Complexity Analysis

* **Time Complexity**: , where  is the total number of nodes in the tree, as we must visit each node once to determine its depth.
* **Space Complexity**:
* **Worst Case**:  for a skewed tree, where the recursion stack grows to the height of the tree.
* **Best Case**:  for a completely balanced tree.



---

## 4. Full Solution

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base Case: An empty tree has a depth of 0
        if not root:
            return 0
        
        # Recursive Step: Get height of subtrees
        left_height = self.maxDepth(root.left)
        right_height = self.maxDepth(root.right)
        
        # The height of current node is the max of its children + 1
        return max(left_height, right_height) + 1

```

### Alternative: Iterative BFS

You can also solve this using the **Level Order** logic we used for the previous problem. Every time you finish processing a full "level" in your queue, you increment a `depth` counter.

```python
from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            depth += 1
            # Process all nodes at the current level
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                
        return depth

```

Would you like me to explain the difference in "stack" vs "heap" memory usage between these two approaches?