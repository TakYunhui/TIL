# OOP
## 객체지향 프로그래밍
-> 절차지향 프로그래밍: 프로그램을 '데이터'와 '절차'로 구성하는 방식의 패러다임
- 프로그래밍 작성 흐름이 데이터와 절차로 나뉘어져 있다
- 데이터와 해당 데이터를 처리하는 함수(절차)가 분리되며, 함수 호출의 흐름이 중요
- 데이터를 다시 재사용하기보다는 함수가 처음부터 끝까지 실행을 마치는 것이 중요

> 소프트웨어 위기: 하드웨어 발전으로 컴퓨터 계산용량과 문제의 복잡성 증가

=> 객체 지향 프로그래밍
- 절차지향 기반으로 보완!! 반대가 아님!!
- 데이터와 해당 데이터를 조작하는 메서드(함수)를 하나의 객체로 묶어 관리하는 방식의 패러다임

절차 지향 
- 함수 호출의 흐림이 중요
객체 지향
- 데이터와 메서드를 하나의 객체(클래스)로 묶음

### 클래스 Class
- 파이썬에서 '타입'을 표현하는 방법
- 객체를 생성하기 위한 설계도 blueprint
- 데이터와 기능을 함께 묶는 방법을 제공
#### 객체
- 클래스에서 정의한 것을 토대로 메모리에 할당된 것
- '속성'과 '행동'으로 구성된 모든 것
- 속성: 변수
- 행동: 메서드(함수)
- 클래스로 만든 객체 -> 인스턴스
```
가수(클래스) -> 아이유(객체)
1. 아이유는 객체다 (O)
2. 아이유는 인스턴스다 (X)
3. 아이유는 가수(클래스)의 인스턴스다 (O)
```

### 인스턴스.메서드()
```
"hello".upper()
문자열.대문자로()
인스턴스.메서드()
```

#### 객체(object) 특징
- 타입(type): 어떤 연산자와 조작이 가능?
- 속성(attribute): 어떤 데이터를 가지는가?
- 조작법(method): 어떤 행위(함수)를 할 수 있는가?

> 파이썬에서 객체는 속성과 메서드가 결합한 것

## 클래스
- 클래스는 객체(인스턴스)를 찍어낼 뿐
- 행동은 인스턴스가 한다!! 
- 생성자 함수 (__init__): 객체의 초기화 담당, 매직 메서드
- 인스턴스 변수: 인스턴스(객체)마다 독립적인 값을 가지며, 인스턴스가 생성될 때마다 초기화
- 클래스 변수: 모든 인스턴스들이 공유하는 변수
- 인스턴스 메서드: 인스턴스 변수에 접근하고 수정하는 작업 수행

### namespace
- 인스턴스와 클래스 간의 이름 공간
- 클래스를 정의하면, 클래스와 해당하는 이름 공간 생성
- 인스턴스를 만들면 독립적인 이름 공간 생성
- 클래스와 다른 인스턴스 간에는 서로의 데이터나 상태에 직접적인 접근이 불가능
- 클래스 변수(생성자 함수) 활용: 생성된 인스턴스의 수 카운트

### 메서드 종류
#### 인스턴스 메서드
- 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드(행동)
- 인스턴스의 상태를 조작하거나 동작을 수행
```python
class MyClass:
  def instance_method(self, arg1, ...):
    pass
```
- 반드시 첫 번째 매개변수로 인스턴스 자신(self)을 전달받음
- self는 매개변수로 암묵적인 약속으로 가지는 이름임!!
#### 생성자 메서드
- 인스턴스 객체가 생성될 때 자동 호출
- 인스턴스 변수들의 초기값 설정

#### 클래스 메서드
- 클래스가 호출하는 메서드
- 클래스 변수를 조작하거나 클래스 레벨의 동작을 수행
- @classmethod 데코레이터 필수! 없으면 인스턴스 메서드 됨
- cls를 매개변수로 작성 -> 상속 때문에?

#### 스태틱(정적) 메서드
- 클래스와 관련이 있는데 ...
-  @staticmethod 이용
- 매개변수 없을 수도 있다!! 일반 함수!! 
- 객체나 클래스 상태 수정 x, 단지 독립적인 행동을 위한 메서드

```
클래스 사용
- 클래스 메서드
- 스태틱 메서드
인스턴스 사용
- 인스턴스 메서드
(* 기능상 모두 메서드 호출은 가능!!하지만 Don't do that)
-> 설계된 이유가 있다, 나중에 유지 보수를 위해 지켜주자
```

#### __str__ 매직 메서드
- 인스턴스 출력 형식을 바꿔줌
#### 데코레이터 @
- 다른 함수의 코드를 유지한 채로 수정하거나 확장하기 위해 사용되는 함수