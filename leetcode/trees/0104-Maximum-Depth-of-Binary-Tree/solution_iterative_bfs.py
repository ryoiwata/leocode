# --- STEP 1: Define the structure ---
from collections import deque
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # This is the magic part that formats your print output
    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

def build_tree(values):
    if not values:
        return None
    
    # 1. Create the root from the first element
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1  # Pointer to move through the list
    
    while queue and i < len(values):
        current_node = queue.popleft()
        
        # 2. Assign Left Child
        if i < len(values) and values[i] is not None:
            current_node.left = TreeNode(values[i])
            queue.append(current_node.left)
        i += 1
        
        # 3. Assign Right Child
        if i < len(values) and values[i] is not None:
            current_node.right = TreeNode(values[i])
            queue.append(current_node.right)
        i += 1
        
    return root

# --- STEP 2: Your Algorithm (Maximum Depth with Logging) ---
class Solution:
    def maxDepth(self, root: Optional[TreeNode], current_depth=0) -> int:
        # Create an indentation prefix based on recursion depth for easy reading
        indent = "  " * current_depth
        
        if not root:
            print(f"{indent}-> Found None: Returning depth 0")
            return 0
        
        print(f"{indent}-> Visiting Node: {root.val}")
        print(f"{indent}   Full Node structure: {root}")

        # Recursive Step: Get height of subtrees
        print(f"{indent}   Exploring LEFT child of {root.val}...")
        left_h = self.maxDepth(root.left, current_depth + 1)
        
        print(f"{indent}   Exploring RIGHT child of {root.val}...")
        right_h = self.maxDepth(root.right, current_depth + 1)
        
        # Result calculation
        max_h = max(left_h, right_h) + 1
        print(f"{indent}<- Finished Node {root.val}: Left Height={left_h}, Right Height={right_h}.")
        print(f"{indent}   Result for this subtree (max + 1): {max_h}")
        
        return max_h

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # The raw input from the problem image
    raw_input = [3, 9, 20, None, None, 15, 7] 
    
    # Build the tree objects
    tree_root = build_tree(raw_input)
    
    print("--- Starting Maximum Depth Calculation ---")
    sol = Solution()
    result = sol.maxDepth(tree_root)
    
    print(f"\nFinal Calculated Maximum Depth: {result}")