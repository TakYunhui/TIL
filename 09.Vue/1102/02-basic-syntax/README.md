# Template Syntax
- DOM을 기본 구성 요소 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 기반 템플릿 구문 사용 
- Vue instance와 DOM 연결, 확장된 문법 제공
```
1. Template Interpolation
{{ msg }}
데이터 바인딩의 가장 기본적인 형태
이중 중괄호 구문(콧수염 구문)

2. Raw HTML
<div v-html="rawHtml"> 
콧수염 구문을 일반 텍스트로 해석하기에 v-html 사용 필요 

3. Attribute Bindings
<div v-bind:id="dynamicId">
콧수염 구문은 HTML 속성 내에서 사용할 수 없어서 v-bind 사용 
HTML id와 vue의 dynamicld속성을 동기화
바인딩 값이 null이나 undefined인 경우 렌더링 요소에서 제거


4. JS Expressions
JS 표현식의 모든 기능 지원
return 뒤에 사용할 수 있는 코드여야 한다 
```

## Directive
: v- 접두사가 있는 특수 속성
- 단일한 표현식이 들어가야 한다 (예외: v-for, v-on)
- 표현식 값이 변경될 때 DOM에 반응적으로 업데이트 적용
```
v-on:submit.prevent="onSubmit"
preventDefault 의 prevent 느낌... 
```
### Arguments
- directive 뒤에 :으로 표시되는 인자 사용 가능
### Modifiers
- .으로 표시되는 특수 접미사, directive가 특별한 방식으로 바인딩되어야 함을 나타냄 


### Dynamically data binding
- v-bind: => : 로 축약 가능
- 동적 인자 이름, [key]="myValue"
- 대괄호 안에는 반드시 소문자로만 구성

## Class and Style Bindings
- 객체 또는 배열 활용 
### Class
1. 객체를 :class에 전달
- 객체의 값이 True/False냐에 따라 key값 넣기
- :class="{ active: isActive}"
2. class를 배열에 바인딩하여 클래스 목록 적용
- :class="[active, hasInfor]"


### v-model
한국어, 중국어, 일본어는 이거 말고 그냥 다 쓰는 거 쓰는 게 동시에 나타난다 
