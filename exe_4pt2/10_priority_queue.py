import heapq
from random import shuffle, choice
  
# let's say we have a list of activities [(priority, task)]
activities = [(30, 'cleaning'),
              (-1, 'prepare food'),
              (100, 'study'),
              (10, 'reading'),
              (20, 'shopping')]

# and also some events to be performed based on the circumstances
events = [(-40, "interphone"),
          (-30, "phone call")]
shuffle(events)
  
# let's organize the activities in a Min Heap based on priority
heapq.heapify(activities)
  
print(f"activities:\t{activities}")
print(f"tasks:\t{events}")

while len(activities) != 0:

    # rescheduling
    if choice([0,1]):
        if len(events) > 0:
            heapq.heappush(activities, events.pop())
    
    print(f"Do {heapq.heappop(activities)[1]}...")
