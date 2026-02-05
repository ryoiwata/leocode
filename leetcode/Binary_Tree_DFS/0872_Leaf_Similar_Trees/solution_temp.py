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
    def getLeafNodes(self, root: Optional[TreeNode]) -> int:
        # Indentation for visual depth in console
        # indent = "  " * depth
        
        if not root:
            # print(f"{indent}-> Found None: Returning depth 0")
            return 0

        print("\nroot")
        print("\t", root)

        leaf_nodes = []
        if root.left:
            print("\t-> Visiting Node: ", root.val)
            print("\tleft")
            print("\t\t", root.left)
            leaf = self.getLeafNodes(root.left)
            leaf_nodes.append(leaf)
            print("\tleaf_nodes", leaf_nodes)
                
        if root.right:
            print("\t-> Visiting Node: ", root.val)
            print("\tright")
            print("\t\t", root.right)
            self.getLeafNodes(root.right)

        else:
            print("\t-> Visiting Node: {root.val}")
            print("\t\tI'm a leaf node", root.val)
            return root.val

        # print(f"-> Visiting Node: {root.val}")
        # print(f"   Full structure here: {root}")


# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # Example 1: root = [3,9,20,null,null,15,7]
    raw_input = [3,5,1,6,2,9,8,None,None,7,4]
    
    print("--- Building Tree ---")
    tree_root = build_tree(raw_input)
    print(f"Tree built: {tree_root}\n")
    
    print("--- Starting Depth Calculation ---")
    sol = Solution()
    output = sol.getLeafNodes(tree_root)
    
    # print(f"\nFinal Maximum Depth: {output}")