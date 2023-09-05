# 분할정복법
- 큰 문제를 작은 문제로 분할해 재귀적으로 해결 
```py
# n제곱 구하기
def power(a, n):
  if n == 0:
    return 1
  x = power(a, n//2)
  if n % 2 == 0:
    return x * x
  else:
    return x * x * a
```
- O(log n)

## 이진탐색
- 오름차순으로 정렬된 n개의 숫자가 저장된 배열 A에서
- 어떤 값 x가 배열에 있는지 없는지 O(log n)에 알 수 있는 탐색법
```
1. 현재 탐색 범위가 A[i], ..., A[j]라면 중간값 A[(i+j)//2] 와 x 를 비교하여 범으로 반으로 줄임
2. 한 번의 비교로 탐색 범위가 반씩 줄기에 (log n + 1)번 이하의 비교로 x 존재 여부 결정 가능 
```
```py
def binary_search(A, i, j, x):
  if i > j:
    return -1
  m = (i+j)//2
  if x == A[m]: # x 찾음
    return m
  elif x < A[m]: # x가 오른쪽 반에는 없으니 왼쪽범위에서탐색 계속(재귀호출)
    return binary_search(A, i, m-1, x)
  else:
    return binary_search(A, m+1, j, x)
```

## Fibonacci 수 계산
1. 피보나치수를 재귀함수로 그대로 구현 
- 간단하나 수행시간이 O(g ^ n)
2. 세 변수만을 이용해 n번째 수 계산하기
- O(n)
3. 배열에 0번째 수부터 n번째 수까지 차례대로 채우기
- for 루프를 이용하여 O(n) 시간에 가능
4. power(a, n) = a^n을 O(log n) 시간에 계산하는 방법을 응용
```py
# 재귀
def fibo_rec(n):
  if n <= 1:
    return 1
  return fibo_rec(n-1) + fibo_rec(n-2)

# 세 변수 
def fibo_three(n):
  f1 = 0
  f2 = 1
  for i in range(2, n+1):
    f3 = f1 + f2
    f1 = f2 
    f2 = f3 
  return f2 

# 배열
def fibo_array(n):
  F = [0, 1]
  for i in range(2, n+1):
    F.append(F[i-1] + F[i-2])
  return F[n]
```

## 하노이 탑
- move(n, A, B, C): A 막대에 있는 n개의 원반을 B막대를 자유롭게 이용해서 C막대로 최소 횟수로 옮김
- move(n-1, A, C, B): A에 있는 가장 위에 있는 n-1개의 원반을 B로 (재귀적으로)옮김
- move(1, A, B, C): A에 남은 가장 큰 원반을 C로 옮김
- move(n-1, B, A, C): B에 있는 n-1개의 원반을 (재귀적으로) C로 옮김
- T(n): move(n, A, B, C)의 이동 횟수


