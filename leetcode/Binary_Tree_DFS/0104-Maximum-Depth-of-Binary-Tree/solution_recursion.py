from collections import deque
from typing import Optional

# --- STEP 1: Define the structure ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current_node = queue.popleft()
        if i < len(values) and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1
    return root

# --- STEP 2: Your Algorithm (Recursive DFS) ---
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth=0) -> int:
        # Indentation for visual depth in console
        indent = "  " * depth
        
        if not root:
            print(f"{indent}-> Found None: Returning depth 0")
            return 0
        
        print(f"{indent}-> Visiting Node: {root.val}")
        print(f"{indent}   Full structure here: {root}")

        # Recursive Step: Get height of subtrees
        print(f"{indent}   Checking Left child of {root.val}...")
        left_height = self.maxDepth(root.left, depth + 1)
        
        print(f"{indent}   Checking Right child of {root.val}...")
        right_height = self.maxDepth(root.right, depth + 1)
        
        current_max = max(left_height, right_height) + 1
        print(f"{indent}<- Finished Node {root.val}: Left={left_height}, Right={right_height}. Max depth so far: {current_max}")
        
        return current_max

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # Example 1: root = [3,9,20,null,null,15,7]
    raw_input = [3, 9, 20, None, None, 15, 7]
    
    print("--- Building Tree ---")
    tree_root = build_tree(raw_input)
    print(f"Tree built: {tree_root}\n")
    
    print("--- Starting Depth Calculation ---")
    sol = Solution()
    output = sol.maxDepth(tree_root)
    
    print(f"\nFinal Maximum Depth: {output}")