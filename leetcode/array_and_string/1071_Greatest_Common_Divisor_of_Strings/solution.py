import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        print(f"--- Analyzing str1: '{str1}' and str2: '{str2}' ---")
        
        # Step 1: Check if strings are commutative
        # If str1 + str2 != str2 + str1, no common divisor exists
        check1 = str1 + str2
        check2 = str2 + str1
        print(f"  Check: '{str1}' + '{str2}' == '{str2}' + '{str1}'?")
        
        if check1 != check2:
            print("  Mismatch found! No common divisor string possible.")
            return ""
        
        print("  Strings are compatible.")

        # Step 2: Find GCD of the lengths
        len1, len2 = len(str1), len(str2)
        common_len = math.gcd(len1, len2)
        print(f"  Length of str1: {len1}, Length of str2: {len2}")
        print(f"  GCD of lengths {len1} and {len2} is: {common_len}")

        # Step 3: The result is the prefix of that GCD length
        result = str1[:common_len]
        print(f"  Potential GCD string: '{result}'")
        
        return result

# --- Execution Logic for Testing ---
if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    print("\n[Example 1]")
    print(f"Result: {sol.gcdOfStrings('ABCABC', 'ABC')}")

    # Test Case 2
    print("\n[Example 2]")
    print(f"Result: {sol.gcdOfStrings('ABABAB', 'ABAB')}")

    # Test Case 3
    print("\n[Example 3]")
    print(f"Result: {sol.gcdOfStrings('LEET', 'CODE')}")
    
    # Test Case 4 (Edge case: Common prefix but no divisor)
    print("\n[Example 4]")
    print(f"Result: {sol.gcdOfStrings('AAAAAB', 'AAA')}")