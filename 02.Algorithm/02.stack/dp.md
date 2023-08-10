# DP
- 동적 계획 알고리즘
- 그리디와 같이 최적화 문제 해결
- 작은 부분 문제들을 모두 해결한 후 그 해들을 이용하여 보다 큰 부분 문제들을 해결

### 피보나치 수 DP 적용
- 부분 문제의 답으로 본 문제의 답을 얻을 수 있으므로 최적 부분 구조로 이루어져 있다
- 1. 문제를 부분 문제로 분할
```
Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
Fibonacci(n-1) = Fibonacci(n-2) + Fibonacci(n-3)
Fibonacci(2) = Fibonacci(1) + Fibonacci(0)
```
- 2. 가장 작은 부분 문제부터 해를 구함
- 3. 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용해 상위 문제의 해를 구함 

```python
# DP
def fibo2(n):
  dp = [0] * (n+1)
  dp[0] = 0
  dp[1] = 1
  for i in range(2, n+1):
    dp[i] = dp[i-1] + dp[i-2]

  return dp[n]
```

```python
# 기본: 재귀
def fibo(n):
  if n < 2:
    return n
  else:
    return fibo(n-1) + fibo(n-2)
# fibo(30) 832040 필요한 호출 횟수 2692537
```

```python
# memoization
def fibo(n):
  if n < 2:
    return memo[n]
  else:
    if memo[n] == 0:
      memo[n] = fibo(n-1) + fibo(n-2)
      return memo[n]
N = 30
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
# fibo(30) 832040 59
```