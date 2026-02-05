class GuessGame:
    """Simulates the API provided in the problem."""
    def __init__(self, pick: int):
        self.pick = pick

    def guess(self, num: int) -> int:
        if num > self.pick:
            return -1
        elif num < self.pick:
            return 1
        else:
            return 0

class Solution(GuessGame):
    def guessNumber(self, n: int) -> int:
        print(f"--- Starting Search for the hidden number in range [1, {n}] ---")
        
        low = 1
        high = n
        
        while low <= high:
            # Calculate mid point. 
            # Using (low + high) // 2 is fine in Python, but in some languages 
            # low + (high - low) // 2 prevents integer overflow.
            mid = low + (high - low) // 2
            
            print(f"Current Range: [{low}, {high}] | Guessing: {mid}")
            
            res = self.guess(mid)
            
            if res == 0:
                print(f"  Result: 0 -> Found the pick: {mid}!")
                return mid
            elif res == -1:
                print(f"  Result: -1 -> {mid} is too HIGH. Searching lower half.")
                high = mid - 1
            else: # res == 1
                print(f"  Result: 1 -> {mid} is too LOW. Searching upper half.")
                low = mid + 1
        
        return -1

# --- Execution Logic ---
if __name__ == "__main__":
    # Example 1: n = 10, pick = 6
    n_val = 10
    hidden_pick = 6
    
    # Initialize the solution with the hidden pick
    sol = Solution(hidden_pick)
    
    result = sol.guessNumber(n_val)
    print(f"\nFinal Answer: {result}")