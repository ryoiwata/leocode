from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        print(f"--- Starting Find the Difference of Two Arrays ---")
        print(f"nums1: {nums1}")
        print(f"nums2: {nums2}")
        
        # Step 1: Create sets to get distinct values and fast lookups
        set1 = set(nums1)
        set2 = set(nums2)
        
        print(f"\nDistinct values in nums1: {set1}")
        print(f"Distinct values in nums2: {set2}")
        
        # Step 2: Find elements in set1 not in set2
        # Using list comprehension for clarity
        diff1 = [x for x in set1 if x not in set2]
        print(f"\nElements in nums1 NOT in nums2: {diff1}")
        
        # Step 3: Find elements in set2 not in set1
        diff2 = [x for x in set2 if x not in set1]
        print(f"Elements in nums2 NOT in nums1: {diff2}")
        
        final_output = [diff1, diff2]
        print(f"\n--- Process Finished ---")
        print(f"Final Output: {final_output}")
        
        return final_output

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: nums1 = [1,2,3], nums2 = [2,4,6]
    # Output: [[1,3],[4,6]]
    n1 = [1, 2, 3]
    n2 = [2, 4, 6]
    sol.findDifference(n1, n2)