from collections import deque

# --- STEP 1: Define the structure ---
class RecentCounter:
    def __init__(self):
        # Initialize an empty queue for pings
        self.requests = deque()
        print("Initialized RecentCounter: Queue is empty.")

    def ping(self, t: int) -> int:
        print(f"\n--- ping({t}) ---")
        
        # 1. Add the new request to the queue
        self.requests.append(t)
        print(f"  Added timestamp {t}. Current Queue: {list(self.requests)}")
        
        # 2. Define the range [t - 3000, t]
        lower_bound = t - 3000
        print(f"  Valid Range: [{lower_bound}, {t}]")
        
        # 3. Remove pings that are older than t - 3000
        while self.requests and self.requests[0] < lower_bound:
            removed = self.requests.popleft()
            print(f"  Removing {removed} (Too old)")
            
        # 4. The size of the queue is the number of pings in the range
        count = len(self.requests)
        print(f"  Remaining Pings: {list(self.requests)}")
        print(f"  Count: {count}")
        
        return count

# --- STEP 2: Execution Logic ---
if __name__ == "__main__":
    # Simulate the Example 1 from the problem description
    actions = ["RecentCounter", "ping", "ping", "ping", "ping"]
    params = [[], [1], [100], [3001], [3002]]
    
    output = []
    obj = None
    
    print("Starting Execution...")
    for action, param in zip(actions, params):
        if action == "RecentCounter":
            obj = RecentCounter()
            output.append(None) # Initializing returns None
        elif action == "ping":
            res = obj.ping(param[0])
            output.append(res)
            
    print(f"\nFinal Output: {output}")