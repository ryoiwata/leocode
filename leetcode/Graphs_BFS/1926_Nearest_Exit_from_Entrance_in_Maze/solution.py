from collections import deque
from typing import List

class MazeSolution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])
        start_row, start_col = entrance
        
        print(f"--- Starting BFS from Entrance: [{start_row}, {start_col}] ---")
        
        # Initialize queue: (row, col, current_steps)
        queue = deque([(start_row, start_col, 0)])
        
        # Mark entrance as visited by turning it into a wall
        maze[start_row][start_col] = "+"
        
        # Directions: Up, Down, Left, Right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c, steps = queue.popleft()
            print(f"Exploring Cell: [{r}, {c}] at {steps} steps")
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # 1. Check if neighbor is within bounds
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 2. Check if neighbor is an empty cell
                    if maze[nr][nc] == ".":
                        
                        # 3. Check if neighbor is on the border (an exit)
                        if nr == 0 or nr == rows - 1 or nc == 0 or nc == cols - 1:
                            print(f"  Target EXIT found at: [{nr}, {nc}]!")
                            return steps + 1
                        
                        # 4. If not an exit, it's an internal path; mark as visited and queue it
                        print(f"  Moving to internal cell: [{nr}, {nc}]")
                        maze[nr][nc] = "+"
                        queue.append((nr, nc, steps + 1))
        
        print("  No exit found.")
        return -1

# --- Execution Logic ---
if __name__ == "__main__":
    sol = MazeSolution()
    
    # Example 1
    maze1 = [["+","+",".","+"],[".",".",".","+"],["+","+","+","."]]
    ent1 = [1, 2]
    # Output: 1
    print(f"\nFinal Result (Example 1): {sol.nearestExit(maze1, ent1)}")
    
    print("\n" + "="*40 + "\n")
    
    # Example 3
    maze3 = [[".","+"]]
    ent3 = [0, 0]
    # Output: -1
    print(f"\nFinal Result (Example 3): {sol.nearestExit(maze3, ent3)}")