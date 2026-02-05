import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        print(f"--- Finding the {k}th largest element in {nums} ---")
        
        # Initialize an empty min-heap
        min_heap = []
        
        for i, num in enumerate(nums):
            # Add the current number to the heap
            heapq.heappush(min_heap, num)
            print(f"Step {i+1}: Added {num}. Current Heap: {min_heap}")
            
            # If heap size exceeds k, remove the smallest element
            if len(min_heap) > k:
                removed = heapq.heappop(min_heap)
                print(f"  Heap size > {k}. Popped smallest element: {removed}")
                print(f"  Heap after pop: {min_heap}")
        
        # The top of the heap is the kth largest element
        result = min_heap[0]
        print(f"\nProcessing complete. The top of the heap is: {result}")
        return result

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    print(f"RESULT 1: {sol.findKthLargest(nums1, k1)}")
    print("-" * 50)
    
    # Example 2
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    print(f"RESULT 2: {sol.findKthLargest(nums2, k2)}")