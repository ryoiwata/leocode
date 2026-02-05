from collections import deque
from typing import List

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        num_rooms = len(rooms)
        print(f"--- Starting traversal for {num_rooms} rooms ---")
        
        # Track which rooms we have successfully entered
        visited = set()
        visited.add(0)
        print(f"Unlocked and entered Room 0. Current visited: {visited}")
        
        # Queue for BFS - holds the keys we've found but haven't used to enter a room yet
        # We start with the keys found in Room 0
        queue = deque(rooms[0])
        print(f"Initial keys collected from Room 0: {list(queue)}")
        
        while queue:
            current_key = queue.popleft()
            print(f"\nUsing key for Room {current_key}...")
            
            if current_key not in visited:
                # Enter the room
                visited.add(current_key)
                print(f"  Success! Room {current_key} is now unlocked.")
                
                # Collect new keys from this room
                new_keys = rooms[current_key]
                print(f"  Found keys {new_keys} in Room {current_key}.")
                
                for key in new_keys:
                    if key not in visited:
                        queue.append(key)
                        print(f"    Added key {key} to the collection queue.")
            else:
                print(f"  Room {current_key} was already visited. Skipping.")

        # Result is true if the number of visited rooms matches the total rooms
        success = len(visited) == num_rooms
        print(f"\n--- Process Complete ---")
        print(f"Rooms visited: {sorted(list(visited))}")
        print(f"Total visited count: {len(visited)} | Required: {num_rooms}")
        
        return success

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1 (Expected: True)
    print("TEST CASE 1:")
    example_1 = [[1], [2], [3], []]
    print(f"Result: {sol.canVisitAllRooms(example_1)}\n")
    
    # Test Case 2 (Expected: False)
    print("-" * 30)
    print("TEST CASE 2:")
    example_2 = [[1, 3], [3, 0, 1], [2], [0]]
    print(f"Result: {sol.canVisitAllRooms(example_2)}")