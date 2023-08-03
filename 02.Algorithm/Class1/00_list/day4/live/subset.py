# 라이브 - 부분집합 설명
def print_subset(bit, arr, n):
    total = 0 # 부분집합의 합
    for i in range(n):
        if bit[i]:
            print(arr[i], end=' ')
            total += arr[i]
    print(bit, total)
    
arr = [1, 2, 3, 4]
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i              # 0번 
    for j in range(2):
        bit[1] = j          # 1번
        for k in range(2):
            bit[2] = k      # 2번
            for l in range(2): 
                bit[3] = l  # 3번
                print_subset(bit, arr, 4)  # 생성된 부분집합 출력

n = len(arr)  # 원소의 개수
for i in range(1<<n): # 1<<n: 부분 집합의 개수
    for j in range(n):# 원소의 수만큼 비트를 비교
        if i & (1<<j):# i의 j번 비트가 1인 경우
            print(arr[j], end=',') # j번 원소 출력
    print()
print()