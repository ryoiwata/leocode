https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

To solve **LeetCode 2390: Removing Stars From a String**, you need to process a string containing lowercase English letters and stars (`*`). Each star acts like a "backspace" key, removing itself and the character immediately to its left.

---

### 1. Logic and Strategy: Stack Data Structure

The most efficient way to handle this "last-in, first-out" behavior is using a **Stack**.

**The Process:**

1. **Iterate**: Loop through each character in the input string `s` from left to right.
2. **Add Characters**: If the current character is a letter, push it onto the stack.
3. **Handle Stars**: If the character is a star (`*`), pop the most recent character off the stack (this removes the closest non-star character to its left).
4. **Final Result**: After the loop, join all remaining characters in the stack to form the final string.

---

### 2. Complexity Analysis

* **Time Complexity**: , where  is the length of the string `s`. we visit each character exactly once.
* **Space Complexity**:  in the worst case (if there are no stars), as we store the characters in a stack.

---

### 3. Full Solution (Debug Format)

```python
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

```

### Why a Stack is Perfect Here

In **Example 1**, you can see the stack building up and shrinking:

* `l`, `e`, `e`, `t` are added.
* The first `*` removes `t`.
* The second `*` removes `e`.
* `c`, `o`, `d` are added.
* The third `*` removes `d`.
* `e` is added, leaving `l-e-c-o-e`.

Would you like me to show you how this problem relates to other "undo" or "backspace" type problems in coding interviews?