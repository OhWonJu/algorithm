from collections import deque


queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)

print(queue)
queue.reverse()
print(queue)

l = list(queue)
print(type(queue))
print(type(l))
