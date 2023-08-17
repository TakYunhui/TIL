# 큐 구현
Q = []

Q.append(1) # enqueue(1)
Q.append(2)
Q.append(3)
print(Q.pop(0))
print(Q.pop(0))
print(Q.pop(0))

# 원형 큐의 구현
# rear 값을 조정해 새로운 원소 삽입 자리 마련: rear <- (rear + 1)mod n;
# 그 인덱스에 해당하는 배열원소 cQ[rear]에 item 저장


