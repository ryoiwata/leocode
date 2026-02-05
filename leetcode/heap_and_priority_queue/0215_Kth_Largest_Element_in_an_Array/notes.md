This is a classic interview question that tests your knowledge of data structures. While sorting the array would take , we can do better.

Here is the breakdown for **LeetCode 215: Kth Largest Element in an Array**.

---

### 1. Problem Framing

* **Goal:** Find the  largest element, not the  distinct element (duplicates count).
* **Constraints:** The array size  can be up to , and values range from  to .
* **Edge Cases:** *  (the maximum element).
*  (the minimum element).
* Arrays with all identical values.
* Arrays with negative numbers.



---

### 2. Logic & Strategy: The Min-Heap Approach

To avoid sorting the entire array, we use a **Min-Heap** of size .

1. **Iterate** through the array elements one by one.
2. **Push** the current element into the Min-Heap.
3. **Check Size:** If the heap size exceeds , **Pop** the smallest element (the top of the Min-Heap).
4. **Result:** After processing the whole array, the Min-Heap will contain the  largest elements seen so far. Since it's a Min-Heap, the "smallest of the  largest" (which is the  largest) will be sitting right at the top.

---

### 3. Complexity Analysis

* **Time Complexity:** . We iterate through  elements, and each heap operation (push/pop) takes  time because the heap never grows larger than .
* **Space Complexity:**  to store the heap.

---

### 4. Full Solution

```python
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

```

Would you like me to explain the **QuickSelect** algorithm, which can achieve an average time complexity of  for this same problem?