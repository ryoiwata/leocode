from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        print(f"--- Starting Find the Highest Altitude ---")
        print(f"Input gains: {gain}")
        
        # Biker starts at altitude 0
        current_altitude = 0
        max_altitude = 0
        
        print(f"Initial State: Altitude = {current_altitude}, Max = {max_altitude}")
        
        # Process each net gain in altitude
        for i, g in enumerate(gain):
            current_altitude += g
            
            print(f"\n[Point {i+1}] Net Gain: {g}")
            print(f"  New Altitude: {current_altitude}")
            
            if current_altitude > max_altitude:
                print(f"  *** New Highest Altitude! Old Max: {max_altitude}, New Max: {current_altitude} ***")
                max_altitude = current_altitude
            else:
                print(f"  Current Max remains: {max_altitude}")
        
        print(f"\n--- Process Finished ---")
        print(f"Final Highest Altitude: {max_altitude}")
        
        return max_altitude

# --- Execution Logic ---
if __name__ == "__main__":
    sol = Solution()
    
    # Example 1: gain = [-5,1,5,0,-7]
    # Expected altitudes: [0, -5, -4, 1, 1, -6]
    example_gain = [-5, 1, 5, 0, -7]
    sol.largestAltitude(example_gain)