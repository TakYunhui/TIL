# 기초 문법 1 
## 표현, 평가, 문장
- 표현식 expression: (), (), () 등을 조합하여 계산되고 결과를 내는 코드 구조
> 표현식이 ()되어 값이 반환됨
- 평가 evaluate: 표현식이나 문장을 ()으로 평가하여 프로그램의 ()을 결정
- 문장 statement: 실행가능한 ()을 기술하는 코드 
   - 종류: (), (), () 등

## 타입과 변수
- 타입 Type: 값이 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의
   - 타입의 구성 요소: () + ()
#### 산술 연산자 
```python
# 실행 결과를 맞추시오 
a = 11
b = 2 
c = -3
print(a // b)
print(a % b)
print(b ** 3)
print(-b ** 2)
print(c ** 2)
```
- 변수 Variable: 값을 ()하는 이름
  - 변수명 규칙
      1. (), 언더스코어(), ()로 구성
      2. ()로 시작할 수 없음
      3. 대소문자 구분
      4. 파이썬 내부 ()는 사용할 수 없음
```python
# 다음 중 오류가 나는 경우를 찾으시오
1 = a
best_python = 100
False = 'fail'
```
- 객체 Object: 타입을 갖는 () 내 값
> 변수는 그 변수가 참조하는 객체의 ()를 가짐
- 할당문 
```python
# 실행 결과를 맞추시오
a = 100
print(a)
a = '백'
print(a)

number = 5
squared = number ** 2
print(squared)

number = 10
print(squared) 
```
- 주석의 목적에 대해 서술하시오

# 기초 문법 2 
## Data Types
### Data Types: 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
#### Numeric Type
- int: ()를 표현하는 자료형
```python
# 진수 표현
print(0b10) 
print(0o30) 
print(0x10) 
```
- float: ()를 표현하는 자료형, ()에 대한 ()   
```
실수 연산 시 예상치 못한 결과가 나오기도 한다.
이러한 증상 발생 이유과 해결책에 대해 적으시오.
```
```python
# 결과를 예상하시오
number = 314e-2
# float
print(type(number)) 
print(number)
```