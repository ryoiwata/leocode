from collections import deque
from typing import Optional, List

# --- STEP 1: Define the structure ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # Formats print output to show nested structures
    def __repr__(self):
        return f"TreeNode{{val: {self.val}, left: {self.left}, right: {self.right}}}"

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

# --- STEP 2: Your Algorithm (Recursive DFS) ---
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        
        def get_leaves(node, leaves, tree_label, depth=0):
            indent = "  " * depth
            if not node:
                return
            
            print(f"{indent}[{tree_label}] Visiting Node: {node.val}")
            
            # Identify if the current node is a leaf
            if not node.left and not node.right:
                print(f"{indent}*** FOUND LEAF: {node.val} ***")
                leaves.append(node.val)
                return

            # Explore Left branch first
            if node.left:
                print(f"{indent}  Checking Left child of {node.val}...")
                get_leaves(node.left, leaves, tree_label, depth + 1)
            
            # Explore Right branch second
            if node.right:
                print(f"{indent}  Checking Right child of {node.val}...")
                get_leaves(node.right, leaves, tree_label, depth + 1)

        print("--- Starting Leaf Extraction ---")
        leaves1, leaves2 = [], []
        
        print("\n>>> Processing Tree 1 <<<")
        get_leaves(root1, leaves1, "Tree 1")
        
        print("\n>>> Processing Tree 2 <<<")
        get_leaves(root2, leaves2, "Tree 2")
        
        print("-" * 30)
        print(f"Final Leaf Sequence 1: {leaves1}")
        print(f"Final Leaf Sequence 2: {leaves2}")
        
        is_similar = leaves1 == leaves2
        print(f"Comparison Result: {'MATCH' if is_similar else 'NO MATCH'}")
        
        return is_similar

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # Example 1 from the problem description
    # Tree 1: [3, 5, 1, 6, 2, 9, 8, null, null, 7, 4]
    t1_input = [3, 5, 1, 6, 2, 9, 8, None, None, 7, 4]
    # Tree 2: [3, 5, 1, 6, 7, 4, 2, null, null, null, null, null, null, 9, 8]
    t2_input = [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8]
    
    root1 = build_tree(t1_input)
    root2 = build_tree(t2_input)
    
    sol = Solution()
    result = sol.leafSimilar(root1, root2)
    
    print(f"\nFinal Boolean Output: {result}")