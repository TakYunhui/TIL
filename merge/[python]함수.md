# Function
```
def add(a, b): # 함수 정의(매개변수):
  c = a + b    # 함수 기능
    return c   # 함수 값 반환
```
- return 값이 둘 이상이 될 수도 있다 (예: divmod(a, b))
- (1, 2) tuple 형태로 리턴

## mutable/immutable
- assignment: value는 복사되지 않고, 참조 주소가 복사된다 
### immutable types: numbers(int, float), string, tuples
```py
a = 10
b = a  # a, b both refer to the object 10
b += 1
print(a, b) # a : 10, b : 11
```
- a, b 모두 immutable이라 b가 바뀌면 a도 바뀔 것 같지만, 그렇지 않음
- immutable? a가 가르키는 객체는 변하지 않는다 
- 즉, a를 통해서만 a의 값이 변경된다 (예: a = a*2)
### mutable types: list, dict
```py
list1 = [1, 2, 3, 4]
list2 = list1
list2[1] = 10
print(list1) # [1, 10, 3, 4]
```
- mutable인 경우에 다른 데서 변경 가능 
- 함수를 통해서도 변경 가능
### default parameter 
```py
def foo(a, b=15, c=27):
  foo(1, 2, 3) # a = 1 b = 2 c =3
  foo(1)       # a = 1 b = 15 c = 27
  foo(1, 2)    # a = 1 b = 2 c = 27

def foo(a, b=15, c) # illegal
```
- 기본인자(키워드인자)가 뒤로 오도록... 
- return 문이 없다면 python은 None을 자동 리턴

## Recursion
```py
# 기본 선형 재귀
def fac(n):
  if n == 1:
    return n
  else:
    return n * fac(n-1)
```
- 리턴되는 값을 가지고 계속 계산하며 완성 (recursion stack 사용)
```py
# 꼬리 선형 재귀
def fac(n, value = 1):
  if n == 1:
    return value
  else:
    return fac(n-1, value * n)
```
- 재귀 함수의 매개변수로 현재 factorial의 값을 직접 전달하기에 n = 1 인 경우에 계산된 최종 값 24가 return 되어 단순히 반복 전달됨
- 이를 이용하여 하나의 recursion stack 내용을 overwrite하는 식으로 메모리 사용을 크게 줄일 수 있다(TRO: 언어에 따라 지원 여부 결정)
