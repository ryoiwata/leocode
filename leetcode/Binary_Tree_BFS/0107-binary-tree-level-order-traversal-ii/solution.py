# --- STEP 1: Define the structure ---
from collections import deque

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

# --- STEP 2: Your Algorithm ---
class Solution:
    def levelOrderBottom(self, root):
        if not root:
            print("Tree is empty.")
            return []
        
        print("Original root: {}".format(root))

        result = []
        queue = deque([root])
        print("\nOriginal queue: {}".format(queue))
        level_count = 0
        
        print(f"\n--- Starting BFS Traversal ---")
        
        while queue:
            level_count += 1
            level_size = len(queue)
            current_level_values = []
            
            print(f"\n[Level {level_count}]")
            print(f"  Nodes in queue to process: {[n.val for n in queue]}")
            print(f"  Level Size: {level_size}")
            
            # Process all nodes at the current depth
            for i in range(level_size):
                print("    Iteration {} of {} levels".format(i + 1, level_size))
                print("    Current queue: {}".format(queue))
                node = queue.popleft()
                print("    Current queue after popleft: {}".format(queue))
                print("    Node that's popped: {}".format(node))

                current_level_values.append(node.val)
                print("    Current Level Values: {}".format(current_level_values))
                print(f"    Processing node: {node.val}")
                
                # Add children to the queue for the next level
                if node.left:
                    print(f"      -> Adding Left child: {node.left.val}")
                    queue.append(node.left)
                if node.right:
                    print(f"      -> Adding Right child: {node.right.val}")
                    queue.append(node.right)
                print("    Current queue after appending: {}".format(queue))

            
            # Append the current level's values to our result
            result.append(current_level_values)
            print(f"  Finished Level {level_count}. Level values: {current_level_values}")
            print(f"  Current results: {result}")
            print(f"  Queue state for next level: {[n.val for n in queue]}")
            
        print(f"\n--- BFS Finished ---")
        print(f"Top-down result: {result}")
        
        final_output = result[::-1]
        print(f"Bottom-up result (reversed): {final_output}")
        
        return final_output

# --- STEP 3: Execution Logic ---
if __name__ == "__main__":
    # The raw input
    raw_input = [3, 9, 20, None, None, 15, 7] # null in JS/JSON is None in Python
    
    # Build the tree objects
    tree_root = build_tree(raw_input)
    
    # Run the solution
    sol = Solution()
    output = sol.levelOrderBottom(tree_root)
    
    print(f"Final Output: {output}")