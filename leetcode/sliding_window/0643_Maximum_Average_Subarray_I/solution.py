from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        print(f"--- Starting Maximum Average Subarray I ---")
        print(f"Input nums: {nums}, k: {k}")
        
        # Step 1: Calculate the sum of the first window
        current_sum = sum(nums[:k])
        max_sum = current_sum
        
        print(f"\nInitial Window (indices 0 to {k-1}): {nums[:k]}")
        print(f"Initial Sum: {current_sum}")
        
        # Step 2: Slide the window across the rest of the array
        for i in range(k, len(nums)):
            entering = nums[i]
            exiting = nums[i - k]
            
            # Update the sum by adding the new element and removing the old one
            current_sum += entering - exiting
            
            print(f"\n[Index {i}] Sliding Window:")
            print(f"  Element entering: {entering}")
            print(f"  Element exiting: {exiting}")
            print(f"  New Window Sum: {current_sum}")
            
            if current_sum > max_sum:
                print(f"  *** New Max Sum Found! Old: {max_sum}, New: {current_sum} ***")
                max_sum = current_sum
            else:
                print(f"  Max Sum remains: {max_sum}")

        # Step 3: Return the max average
        final_average = max_sum / k
        print(f"\n--- Process Finished ---")
        print(f"Max Sum: {max_sum}, Max Average: {final_average}")
        
        return final_average

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums = [1,12,-5,-6,50,3], k = 4
    example_nums = [1, 12, -5, -6, 50, 3]
    example_k = 4
    example_nums = [5]
    example_k = 1
    sol.findMaxAverage(example_nums, example_k)