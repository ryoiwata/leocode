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