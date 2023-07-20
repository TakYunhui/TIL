# 반복문 
## 반복문 안의 반복문
### 예: while문 안의 for문

```python
while True:
  print('while')
    for i in range(5):
      print('for')
      

'''
  1. while 출력
  2. for 문 끝날 때까지 출력 -> forforforforfor 
  3. 다시 while로 돌아가 true면 while 출력
  ... 
  => while
     for
     for
     for
     for
     for
     while
     for
     for
     .
     .
     .
'''
```

## iterable 
- 순회가능한 자료형 
- 시퀀스 자료형 + dict + set
- non-iterable -> int 등...

### list
-> sequence type data: 순서가 있다.
-> 길이(개수)를 알 수 있다. len(list)

### range
-> 0 ~ n-1 까지의 숫자 범위를 만들 수 있다.
-> sequence type, iterable

### for 특성
-> iterable한 값이 가지고 있는 각 요소들을, 임시 변수에 할당해서 코드를 실행
-> for문으로 range를 순회 하면, range가 가지고 있는 0부터 n-1 까지의 값을 순회