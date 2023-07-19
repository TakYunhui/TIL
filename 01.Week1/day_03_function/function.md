# 함수
- 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
  1. 목적을 가지고 있다
  2. 재사용이 가능하다
> 함수를 사용하는 이유: 재사용성, 가독성과 유지보수성 향상

## 내장 함수
- built-in function
- 파이썬이 기본적으로 제공하는 함수
- 별도의 import 없이 바로 사용 가능
```python
# 함수 호출의 반환값을 절대값으로 바꿈
result = abs(-1)
print(result) # 1
```
[파이썬공식문서](https://docs.python.org/ko/3/)
-자습서와 라이브러리 참고

## 함수 호출
- function call
- 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드를 불러오는 것

```python
# 함수 구조
def make_sum(pram1, pram2):
  """이것은 두 수를 받아
  두 수의 합을 반환하는 함수입니다.

  >>> make_sum(1, 2)
  3
  """
  return pram1 + pram2
```
- parameter: 매개변수
- Docstring(문서 문자열): 함수에 대한 설명
- return value(반환값): 함수가 반환해주는 값

### 함수의 정의 
1. 함수 정의는 def 키워드로 시작
2. def 키워드 이후 함수 이름 작성
3. 괄호 안에 매개변수 정의할 수 있음
4. 매개변수는 함수에 전달되는 값을 나타냄
5. 함수 body 부분 정의
   - 콜론(:) 다음에 들여쓰기 된 코드 블록
   - 함수가 실행될 때 수행되는 코드를 정의
   - Docstring은 함수 body 앞에 선택적으로 작성 가능한 함수 설명서

6. 함수 반환 값 
   - 필요한 경우 결과를 반환할 수 있음
   - return 키워드 이후 반환 값 명시
   - return 문은 함수의 실행을 종료, 결과를 호출 부분으로 반환
   > 반환값이 없는 함수는 return이 None


### 매개변수와 인자
#### 매개변수 
- parameter: 함수를 정의할 때, 함수가 받을 값을 나타내는 변수
#### 인자
- argument: 함수를 호출할 때, 실제로 전달되는 값

```python
def add_numbers(x, y): # parameter
  result = x + y
  return result

a = 2
b = 3
sum_result = add_numbers(a, b) # argument
```
1. 위치인자: 함수 호출 시 인자의 위치에 따라 전달되는 인자 
   - 위치인자는 함수 호출 시 반드시 값을 전달해야 함 
2. 기본 인자 값: 함수 정의에서 매개변수에 기본 값을 할당하는 것 
     - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨
3. 키워드인자: 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
4. 임의의 인자 목록
- 정해지지 않은 개수의 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '*'를 붙여 사용하며, 여러 개의 인자를 tuple로 처리
5. 임의의 키워드 인자 목록
- 정해지지 않은 개수의 키워드 인자를 처리하는 인자
- 함수 정의 시 매개변수 앞에 '**' 붙여 사용하며, 여러 개의 인자를 dictionary로 묶어서 처리

#### 함수 인자 권장 작성순서
위치 > 기본 > 가변 > 키워드 > 가변키워드
> pos1, pos2, default_arg='default', *args, kwd, **kwargs
```python
# *objects 가변인자
# sep=' ', end='\n', file=sys.stdout, flush=False 4개의 기본인자
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

# Scope 
- 함수는 코드 내부에 local scope를 생성
- 그 외의 공간인 global scope로 구분
1. global scope: 코드 어디에서든 참조할 수 있는 공간
2. local scope: 함수가 만든 scope(함수 내부에서만 참조 가능)
   - local에 있는 것은 global에서 참조 불가능

### 변수 수명 주기 lifecycle
1. built-in scope: 파이썬이 실행된 이후부터 영원히 유지
2. global scope: 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지
3. local scope: 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

### 이름 검색 규칙(Name Resolution)
#### LEGB Rule 
- 안쪽 -> 바깥 순서로 찾음
- 역으로는 불가능
1. Local scope: 지역 범위(현재 작업중인 범위)
2. Enclosed scope: 지역 범위 한 단계 위 범위
3. Global scope: 최상단에 위치한 범위
4. Built-in scope: 모든 것을 담는 범위(정의하지 않고 사용할 수 있음)

#### global 키워드
- 변수의 스코프를 전역 범위로 지정, 일반적으로 함수 내에서 전역 변수를 수정하려는 경우에 사용     
    - global 키워드 선언 전에 접근 x
    - 매개변수에 global 사용 x
> 가급적 사용 x, 함수로 값을 바꾸고자 한다면 항상 인자로 넘기고 함수의 반환 값을 사용하는 것을 권장

# 재귀 함수
- 특정 알고리즘 식을 표현할 때 사용
- 중복되는 변수 사용을 줄이고, 특정 알고리즘을 직관적으로 표현 가능
- 대표적인 예시: n! 
> 함수가 자기 자신의 함수를 호출하는 함수
1. 종료 조건을 명확히
2. 반복되는 호출이 종료 조건을 향하도록 (무한 호출 주의)


# 유용한 내장 함수
1. map(function, iterable)
- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수를 적용하고, 그 결과를 map object로 반환
- 내가 만든 함수를 map에서 각각의 요소에 적용되게 사용할 수 있음
2. zip(*iterables)
- 임의의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
3. lambda 함수
- 이름 없이 정의되고 사용되는 익명 함수
> lambda 매개변수: 표현식
- lambda 키워드: 람다 함수 선언 키워드
- 매개변수: 함수에 전달되는 매개변수들, 여러 개 있을 경우 쉼표로 구분
- 표현식: 함수의 실행되는 코드 블록, 결과값을 반환하는 표현식