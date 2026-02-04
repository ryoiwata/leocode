class Solution:
    def removeStars(self, s: str) -> str:
        print(f"--- Starting Removing Stars From a String ---")
        print(f"Input string: '{s}'")
        
        stack = []
        
        # Process each character one by one
        for i, char in enumerate(s):
            if char == '*':
                if stack:
                    removed = stack.pop()
                    print(f"[Index {i}] Found '*': Removing '{removed}' from left.")
            else:
                stack.append(char)
                print(f"[Index {i}] Found '{char}': Adding to stack.")
            
            # Show current stack state for debugging
            print(f"  Current stack: {''.join(stack)}")

        final_output = "".join(stack)
        print(f"\n--- Process Finished ---")
        print(f"Final Output: '{final_output}'")
        
        return final_output

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: s = "leet**cod*e"
    # Expected Output: "lecoe"
    example_input = "leet**cod*e"
    sol.removeStars(example_input)