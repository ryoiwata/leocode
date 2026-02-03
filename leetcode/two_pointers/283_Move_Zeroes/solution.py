from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        print(f"--- Starting Move Zeroes ---")
        print(f"Original array: {nums}")
        
        last_non_zero = 0
        
        # Iteration through the array
        for i in range(len(nums)):
            print(f"\n[Index {i}] Value: {nums[i]}")
            
            if nums[i] != 0:
                print(f"  Non-zero found! Swapping nums[{i}] with nums[{last_non_zero}]")
                # Swap elements
                nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
                
                last_non_zero += 1
                print(f"  Next non-zero write position: {last_non_zero}")
            else:
                print(f"  Zero found at index {i}. Skipping swap.")
            
            print(f"  Current array state: {nums}")

        print(f"\n--- Process Finished ---")
        print(f"Final Output: {nums}")

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [0,1,0,3,12]
    example_input = [0, 1, 0, 3, 12]
    sol.moveZeroes(example_input)