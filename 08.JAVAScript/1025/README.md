# 참조 자료형
- 참조 자료형: 주소 값이 저장
- 객체의 주소가 저장되기에 가변적 
## 함수 
```JS
function name([parm]) {
  statements
  return value
}
```
- return이 없다면 undefined 반환
- 선언식 + 표현식 
```js
const sub = function (num1, num2) {
  return num1 - num2
}
sub(2,1) // 1
```
- 표현식 특징
```
1. 함수 이름이 없는 익명 함수 가능
2. 선언식과 달리 호이스팅이 되지 않기에 함수를 정의하기 전에 먼저 사용 불가
```
- 표현식 사용이 권장된다

### 매개변수
1. 기본 함수 매개변수
- default 값 주기
- 값이 없거나 undefined가 전달될 때 이름 붙은 매개변수를 기본값으로 사용
2. 나머지 매개변수 (가변인자 받기)
- 임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타낸다
- 함수 정의에서 매개변수 마지막에 위치해야 한다
#### 매개변수와 인자 개수 불일치
1. 매개변수 > 인자
- 누락된 인자는 undefined로 할당
2. 매개변수 < 인자
- 초과 입력한 인자는 사용 X

### 전개 구문 Spread Syntax (...)
- 배열이나 문자열과 같이 반복 가능한 항목 펼치지 
- 확장 : 함수 호출 시, 인자 확장
- 전개
- 배열이나 객체 요소를 개별 값으로 분리/다른 배열이나 객체 요소를 현재 배열이나 객체에 추가
- 나머지 매개변수(압축)

### 화살표 함수
- 함수 표현식의 간결한 표현법 (=>)
```
[작성 과정]
1. function 키워드 제거 후 매개변수와 중괄호 사이 화살표 => 작성
2. 함수의 매개변수가 하나뿐이라면 () 소괄호 제거 가능 (하지만 생략 안 하는 걸 권장)
3. 함수 body가 1줄이라면 {}와 return 제거 가능
```


## 객체
- 데이터 타입으로써의 객체, 객체지향프로그래밍의 객체가 아니다!
- 키로 구분된 데이터 집합을 저장하는 자료형
- 중괄호를 이용해 작성, key:value 쌍으로 구성된 속성을 여러 개 작성 가능
- key는 문자형만 허용, value는 모든 자료형 허용
```
[접근 방법]
1. '.' chaining operator : 점으로 접근 (ex: user.name)
2. 대괄호[]: user['key with space'] 와 같이 key 이름에 띄어쓰기 구분자가 있으면 대괄호 접근만 가능
```
- method: 객체 속성에 정의된 함수
- object.method() 방식으로 호출, 메서드는 객체를 행동할 수 있게 함
- this keyword: 함수나 메서드를 호출한 객체를 가리키는 키워드 -> 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
```
[호출 방법에 따른 대상]
1. 단순 호출 : 전역 객체 
2. 메서드 호출 : 메서드 공간에 있는 객체 
-> forEach 인자로 작성된 콜백 함수는 단순 호출이므로 this가 전역 객체를 가리킴
-> 화살표 함수는 자신만의 this를 가지지 않기에 외부 함수(상위 함수)에서 this값을 가져옴, 화살표 함수를 사용해 window를 나타내지 않게 한다
```
### this
- 호출 방식에 따라 결정되는 객체
- python self, java this : 선언 시 이미 값이 정해진다
- js this : 함수가 호출되기 전까지 값이 할당되지 않고 호출 시 결정(동적 할당)
- 함수를 하나만 만들어서 여러 객체에서 재사용 가능
- 유연함 때문에 실수가 일어날 수 있음
```
[객체]
1. 단축 속성: 키 이름과 값으로 쓰이는 변수의 이름이 같으면 생략 가능
2. 단축 메서드: 메서드 선언시 function 키워드 생략 가능
3. 계산된 속성: 키가 대괄호[]로 둘러쌓이면 고정 값이 아닌 변수 값을 사용할 수 있음
4. 구조 분해 할당: 배열 또는 객체를 분해해 속성을 변수에 쉽게 할당할 수 있는 문법
5. 전개 구문: "객체 복사" - 객체 내부에서 객체 전개, 얕은 복사에 활용
6. 객체 메서드: Object.keys(), Object.values() -> 결과가 배열로 나온다
7. Optional chaining(?.): 속성이 없는 중첩 객체를 에러없이 접근 가능 -> 코드의 흐름을 멈추지 않는 상태에서 참조 대상이 있는지 없는지 판별 가능 
(유사: user.nonMethod?.() 메서드에서도 사용 가능)
- 참조가 누락될 가능성이 있는 경우 작성 
- 어떤 속성이 필요한지 확실하지 않은 경우 객체를 편리하게 탐색 가능
- 왼쪽 평가대상이 없어도 괜찮은 대상인 경우에만 선택적으로 사용
- optional chaining 앞의 변수는 반드시 선언되어 있어야 함(referenceerror 뜸)
```

### json
- JS Object Notation
- 형식이 있는 '문자열'

### new 연산자
```js
function Member(name, age, sId) {
  this.name = name
  this.age = age
  this.sId = sId
}
```


## 배열 
### Object
- 키로 구분된 데이터 집합을 저장하는 자료형
- 이제 순서가 있는 collection이 필요함 -> Array
### 배열 구조
- [] 이용
- 요소 자료형 제약 x
- length 속성을 사용해 배열에 담긴 요소 개수 확인 가능
- JS는 [-1] index가 없다
### 메서드
1. push/pop : 배열 끝 요소를 추가/제거
2. unshift/shift : 배열 앞 요소를 추가/제거

### Array helper method
- 배열을 순회하며 특정 로직을 수행하는 메서드
- 메서드 호출 시 인자로 함수(콜백 함수)를 받는다
1. forEach : 인자로 주어진 함수를 배열 요소 각각에 대해 실행
```js
arr.forEach(callback(item[, index[, array]]))
```
- item: 처리할 배열 요소
- index: 처리할 배열 요소의 인덱스 
- array: forEach를 호출할 배열
- return 값이 없어 undefined 반환

2. map : 배열 내의 모든 요소 각각에 대해 함수를 호출하고, 함수 호출 결과를 모아 새로운 배열을 반환
- 반환되는 결과를 넣을 변수가 필요
=> return 여부 차이

#### 콜백 함수
- 다른 함수에 인자로 전달되는 함수, 호출하고 다시 부른다~
- 외부 함수 내에서 호출되어 일종의 루틴이나 특정 작업을 진행
1. 함수의 재사용성
2. 비동기적 처리 측면


### 배열 순회 종합
1. for loop
- 배열의 인덱스 이용해 접근
- break, continue 사용 가능
2. for of 
- 배열 요소에 바로 접근 가능
- break, continue 사용 가능
3. forEach 
- 간결하고 가독성 높음
- callback 함수를 이용해 요소 조작에 용이
- break, continue 사용 불가능
- 사용 권장

### 추가 배열 문법
1. array with '전개 구문'
2. filter, find, some, every

#### 배열은 객체다