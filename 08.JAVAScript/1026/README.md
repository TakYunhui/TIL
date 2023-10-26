# Controlling event
- 이벤트를 통해 특정 동작 수행 
- 모든 DOM 요소는 event를 만든다, event를 받고 처리할 수 있음(event handler)
## event handler
- 이벤트가 발생했을 때 실행되는 함수
### .addEventListener(func)
- 특정 이벤트를 DOM요소가 수신할 때마다 콜백 함수를 호출
- 콜백 함수 ? 어떤 외부 함수의 인자로 들어가는 함수
```
EventTarget.addEvenListener(type, handler)
DOM 요소                   수신할 이벤트, 콜백 함수
```
- type: 수신할 이벤트 이름, 문자열로 작성
- handler: 콜백 함수, 발생한 Event object를 유일한 매개변수로 받음
- "버튼을 클릭하면 버튼 요소 출력"
- 버튼에 이벤트 처리기를 부착하여 클릭 이벤트가 발생하면 이벤트가 발생한 버튼 정보 출력
- 아무것도 반환하지 않음 (값 x, 행동 o)

## 버블링
- 한 요소에 이벤트가 발생하면 이에 할당된 핸들러 동작
- 이어서 부모 요소의 핸들링 동작 
- 가장 최상단의 조상 요소(document)를 만날 때까지 이 과정이 반복
### target 
- 실제 이벤트가 시작된 target 요소, 버블링이 진행되어도 불변
### currentTarget
- 현재 요소, 항상 이벤트 핸들러가 연결된 요소만을 참조
- this와 같다

## <-> 캡처링
- 이벤트가 발생한 요소부터 하위 요소로 전파

### click 이벤트
### input 이벤트
- 사용자 입력을 실시간 출력


### .preventDefault()
- 해당 이벤트에 대한 기본 동작을 실행하지 않도록 함