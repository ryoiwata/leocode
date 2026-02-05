from collections import deque
from typing import Optional

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
    def goodNodes(self, root: TreeNode) -> int:
        print(f"--- Starting Count Good Nodes ---")
        
        def dfs(node, current_max, depth=0):
            if not node:
                return 0
            
            indent = "  " * depth
            is_good = 0
            
            # Check if current node is "good"
            if node.val >= current_max:
                print(f"{indent}Node {node.val} is GOOD (>= max {current_max})")
                is_good = 1
            else:
                print(f"{indent}Node {node.val} is NOT good (< max {current_max})")
            
            # Update max for children
            new_max = max(current_max, node.val)
            
            # Recurse left and right
            left_count = dfs(node.left, new_max, depth + 1)
            right_count = dfs(node.right, new_max, depth + 1)
            
            return is_good + left_count + right_count

        # Initial max is set to the smallest possible value based on constraints
        result = dfs(root, float('-inf'))
        
        print(f"\nTotal Good Nodes: {result}")
        return result

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: root = [3,1,4,3,null,1,5]
    # Expected Output: 4
    input_list = [3, 1, 4, 3, None, 1, 5]
    tree_root = build_tree(input_list)
    sol.goodNodes(tree_root)