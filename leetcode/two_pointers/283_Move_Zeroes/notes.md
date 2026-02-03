To solve **LeetCode 283: Move Zeroes**, the goal is to shift all zeroes in an integer array to the end while preserving the original relative order of non-zero elements. This must be done **in-place** without creating a copy of the array.

### 1. Logic and Strategy: Two Pointers

The most efficient way to handle this in-place is using a "read" pointer and a "write" pointer.

* **Write Pointer (`last_non_zero`):** Tracks where the next non-zero element should be placed.
* **Read Pointer (`i`):** Iterates through the entire array.

**The Process:**

1. Iterate through the array with the read pointer.
2. Whenever a non-zero element is found, swap it with the element at the `last_non_zero` position.
3. Increment the `last_non_zero` pointer.

### 2. Complexity Analysis

* **Time Complexity:** , where  is the length of the array. We traverse the array exactly once.
* **Space Complexity:** . No additional data structures are used.

---

### 3. Full Solution (Debug Format)

```python
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

```

### Key Insight

By **swapping** instead of just overwriting, we don't have to manually fill the end of the array with zeroes after the loop. The zeroes naturally "bubble" toward the back as non-zero elements move toward the front.

Would you like me to show you the "two-pass" version of this approach, where we overwrite first and then fill with zeroes at the end?