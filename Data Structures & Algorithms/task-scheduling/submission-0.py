import heapq
from collections import deque, Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # max heap -> (3, 'X')
        ready = [(-count, task) for task, count in Counter(tasks).items()]
        heapq.heapify(ready)

        cooldown = deque()

        cycles = 0
        while ready or cooldown:
            if ready:
                # Move task out of ready 
                neg_remaining, task = heapq.heappop(ready)
                remaining = -neg_remaining - 1 # "Process" the task

                # Move task to cooldown if needed
                if remaining > 0:
                    next_eligible_cycle = cycles + n + 1
                    cooldown.append((task, next_eligible_cycle, remaining))

            # Finish the cycle
            cycles += 1

            # Check if a task can be moved from cooldown to ready for the next cycle
            if cooldown and cooldown[0][1] <= cycles: 
                task, _, remaining = cooldown.popleft()
                heapq.heappush(ready, (-remaining, task))

        return cycles
