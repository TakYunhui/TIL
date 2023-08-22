from queue import PriorityQueue
import heapq
arr = [6, 3, 2, 7, 9, 1]
que = PriorityQueue()
for num in arr:
    que.put(num)
print('----우선순위큐----')
print(que.queue)
print(que.get())
print(que.queue)

heapq.heapify(arr)
print(arr)
heapq.heappush(arr, 5)
print(arr)
print(heapq.heappop(arr))
print(arr)

