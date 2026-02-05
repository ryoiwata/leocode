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