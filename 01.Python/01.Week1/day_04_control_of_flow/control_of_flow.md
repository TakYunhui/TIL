# 제어문
- 위에서 아래로 실행되는코드의 흐름을 
- 멈추게 하거나
- 특정 부분을 반복하게 하는 것
> 특정 조건에 따라 코드 블록을 실행하거나 반복적으로 실행

## 조건문
- 주어진 조건식을 평가해 해당 조건이 참이면 코드 블록을 실행하거나 건너뜀
- if / elif / else
### if statement
```python
if 표현식:
    코드 블록
elif 표현식:
    코드 블록
else:
    코드 블록
```
- elif와 else는 선택적으로 사용 가능
- 조건식은 동시에 검사하는 것이 아니라 if문(위에서)부터 순차적으로 비교

## 반복문
- 주어진 코드 블록을 여러 번 반복해서 실행하는 구문
- 특정 작업을 반복적으로 수행(종료 조건 x)
- 혹은 주어진 조건이 참인 동안 반복 수행(종료 조건 o)
- for / while

### for statement
- 특정한 종료 조건은 없음
- 왜냐? 개수가 있기 때문에 다 돌면 자동 종료
- 임의의 시퀀스의 항목들을 그 시퀀스에 들어있는 순서대로 반복
```python
for 변수 in 반복 가능한 객체:
    코드 블록
```
#### 반복 가능한 객체
- iterable
- 반복문에서 순회할 수 있는 객체
- 시퀀스 객체 + dict, set 포함
- 그럼 dict, set의 요소도 셀 수 있나보다

### while statement
- 주어진 조건식이 참으로 평가받는 동안 코드를 반복해 실행
- == 조건식이 거짓이 될 때까지 반복
```python
while 조건식:
    코드 블록
```



## 적절한 반복문 활용
### for
- 반복 횟수가 명확하게 정해져 있는 경우
- 리스트, 튜플, 문자열 등과 같은 시퀀스 형식 데이터 처리
### while
- 반복 횟수가 불명확하거나 조건에 따라 반복을 종료할 때
- 사용자의 입력을 받아 특정한 조건을 충족시킬 때

## 반복 제어
- for문과 while은 매 반복마다 본문 내 모든 코드를 실행하나...
- 일부만 실행하는 경우가 필요할 때가 있음
### break
- 반복을 즉시 중지
### continue 
- 다음 반복으로 건너뜀

#### break와 continue 남용하면 코드 가독성 저하

## List Comprehension
- 간결하고 효율적인 리스트 생성
#### 리스트 생성
1. [] 빈 리스트에 요소 넣기
2. map + list() 함수 이용
3. list comprehension
```python
[expression for 변수 in iterable]
list(expression for 변수 in iterable)
```

## pass
- 아무런 동작도 수행하지 않고 넘어가는 역할
1. 코드 작성 중 미완성 부분
```python
def my_function():
    pass
```
2. 조건문에서 아무런 동작을 수행하지 않아야 할 때
```python
if condition:
    pass # 아무런 동작도 수행 x
else:
    # 다른 동작 수행
```
3. 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루프를 계속 진행
```python
while True:
    if condition:
        break
    elif condition:
        pass # 루프 계속 진행
    else: 
        print('..')
```

## enumerate
- iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수