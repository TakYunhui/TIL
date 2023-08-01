# Classes 상속
## 상속 Inheritance
- 기존 클래스의 속성과 메서드를 물려받아 새로운 하위 클래스를 생성하는 것
#### 상속이 필요한 이유
1. 코드 재사용
- 상속을 통해 기존 클래스의 속성과 메서드 재사용
- 재정의할 필요 없이 그대로 활용 가능
2. 계층 구조
- 부모 클래스와 자식 클래스 간 관계 설정 가능
3. 유지 보수의 용이성
- 상속을 통해 기존 클래스의 수정이 필요한 경우, 해당 클래스만 수정하면 됨
```python
# 상속 사용

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def talk(self): 
    print(f'반갑습니다. {self.name}입니다.')

# 하위 클래스 정의(상위클래스)
class Professor(Person):
  def __init__(self, name, age, department):
    self.name = name
    self.age = age
    self.department = department

```

### 다중 상속
- 두 개 이상의 클래스를 상속받는 경우
- 상속받은 모든 클래스의 요소 활용 가능
- 중복된 속성이나 메서드가 있으면 상소 순서에 의해 결정됨

#### mro()
- method resolution order
- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인하는 메서드
- 상속에 의한 탐색의 순서

## 오류와 디버깅
### 디버깅
1. print 함수 활용
2. 개발 환경 기능 활용
3. Python tutor 활용(단순 파이썬 코드)
4. 뇌 컴파일, 눈 디버깅 등

### 에러 유형
Syntax Error
- 문법 에러: 구문 자체를 틀리게 쓴 것 
Exception
- 예외: 프로그램 실행 중에 감지되는 에러

> 에러 != 예외

#### 내장 예외
- 예외 상황을 나타내는 예외 클래스들
- 이미 파이썬에 정의되어 있으며, 예외 상황 처리
```python
# ZeroDivisionError: 0으로 나눌 때
10/0

# NameError: 찾고자 하는 변수 이름이 없을 때 - 선언 x, 이름 오타
print(name_error)

# TypeError: 타입 불일치/인자 누락, 초과/인자 타입 불일치
'2' + 2
sum()

# ValueError: 연산이나 함수에 문제 없으나 부적절한 값의 인자를 받았거나 상황이 IndexError처럼 더 구체적인 예외로 설명되지 않는 경우

# IndexError: 시퀀스 인덱스가 범위를 벗어날 때
empty_list = []
empty_list[2]

# KeyError: 딕셔너리에 해당 키가 존재 x

# ModuleNotFoundError: 모듈을 찾을 수 없을 때

# ImportError: 임포트하려는 이름을 찾을 수 없을 때

# KeyboardInterrupt: 사용자가 무한 루프 강제종료시킬 때 

# IndentationError: 들여쓰기 잘못 
```

### 예외 처리 try-except
```python
try:
  예외가 발생할 수 있는 코드

except 예외:
  예외 처리 코드
```
- 에러 클래스 간 상속(계층) 존재
- 계층 구조를 생각해 하위 클래스부터 작성

### 2가지 접근 방식 
1. EAFP: 예외처리를 중심으로 코드를 작성하는 접근 방식
- 일단 지르고 용서를 구함
- try-except 방식
2. LBYL: 값 검사를 중심으로 코드를 작성하는 접근 방식
- if-else 방식 

- as 키워드: 에러 메시지를 except 블록에서 사용할 수 있음