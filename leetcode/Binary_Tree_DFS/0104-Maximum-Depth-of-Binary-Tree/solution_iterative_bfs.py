from collections import deque
from typing import Optional, List

# --- STEP 1: Define the structure ---
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
    # This magic part formats your print output to show nested structures
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

# --- STEP 2: Your Algorithm (Iterative BFS) ---
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            print("Tree is empty. Depth is 0.")
            return 0
        
        print("Original root structure: {}".format(root))

        queue = deque([root])
        depth = 0
        print("\nStarting queue: {}".format(queue))
        
        print(f"\n--- Starting BFS Depth Traversal ---")
        
        while queue:
            # Increment depth for every new level encountered
            depth += 1
            level_size = len(queue)
            
            print(f"\n[Depth/Level {depth}]")
            print(f"  Nodes in queue to process for this depth: {[n.val for n in queue]}")
            print(f"  Level Size: {level_size}")
            
            # Process all nodes currently in the queue for this level
            for i in range(level_size):
                print("    Iteration {} of {} nodes at this depth".format(i + 1, level_size))
                node = queue.popleft()
                print("    Node popped: {} (Full: {})".format(node.val, node))

                # Add children to the queue for the NEXT depth level
                if node.left:
                    print(f"      -> Adding Left child: {node.left.val}")
                    queue.append(node.left)
                if node.right:
                    print(f"      -> Adding Right child: {node.right.val}")
                    queue.append(node.right)
                
                print("    Queue after checking children: {}".format([n.val for n in queue]))

            print(f"  Finished processing Depth {depth}.")
            print(f"  Current Max Depth reached: {depth}")
            
        print(f"\n--- BFS Finished ---")
        return depth

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # Example 1: root = [3, 9, 20, null, null, 15, 7]
    raw_input = [3, 9, 20, None, None, 15, 7] 
    
    # Build the tree objects
    tree_root = build_tree(raw_input)
    
    # Run the solution
    sol = Solution()
    output = sol.maxDepth(tree_root)
    
    print(f"\nFinal Calculated Maximum Depth: {output}")