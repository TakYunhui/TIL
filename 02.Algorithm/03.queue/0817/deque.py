# 덱
from collections import deque
q = deque() # q: deque([3])
q.append(1)
q.append(2)
q.append(3)
print(q.popleft())
print(q.popleft())
print(q.popleft())

