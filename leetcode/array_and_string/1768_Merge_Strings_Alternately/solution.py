class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        print(f"--- Starting Merge ---")
        print(f"word1: '{word1}', word2: '{word2}'")
        
        result = []
        i, j = 0, 0
        m, n = len(word1), len(word2)
        
        # Continue as long as there is at least one character left in either string
        while i < m or j < n:
            # If word1 still has characters, take one
            if i < m:
                print(f"  Adding from word1: '{word1[i]}' (index {i})")
                result.append(word1[i])
                i += 1
            
            # If word2 still has characters, take one
            if j < n:
                print(f"  Adding from word2: '{word2[j]}' (index {j})")
                result.append(word2[j])
                j += 1
            
            print(f"  Current Result: {''.join(result)}")

        final_string = "".join(result)
        print(f"\n--- Merge Finished ---")
        print(f"Final Output: {final_string}")
        
        return final_string

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: word1 = "abc", word2 = "pqr"
    sol.mergeAlternately("abc", "pqr")
    
    # Example 2: word1 = "ab", word2 = "pqrs"
    print("\n" + "="*20 + "\n")
    sol.mergeAlternately("ab", "pqrs")