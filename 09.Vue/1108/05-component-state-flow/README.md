# Component state flow 
## Passing Props
- 컴포너트가 여러 개일 때, 각 컴포넌트가 개별적으로 동일한 데이터를 관리하면 반응형 갱신이 불가능
- 컴포넌트들의 공통된 부모 컴포넌트에서 데이터 관리
- 부모가 자식에게 데이터를 전달(pass props), 자식이 자신에게 일어난 일을 부모에게 알림(emit event)

### props
- 부모로부터 자식에게 데이터를 전달할 때 사용되는 속성
- 부모가 업데이트되면 자식에게 데이터를 주나 그 반대는 안됨 
- One-way data flow: 하향식 단방향 방식
- 단방향인 이유? 하위 컴포넌트가 실수로 상위 컴포넌트의 상태를 변경하여 앱에서 데이터 흐름을 이해하기 어렵게 만드는 것을 방지

```
1. Props 선언
  my-msg="message" // HTML은 '-' 케밥케이스
  prop이름="prop 값" 
  (1) 문자열 배열
  <script setup>
  defineProps(['myMsg']) // JS는 카멜케이스
  </script>

  (2) 객체 배열
  defineProps({
    myMsg: String
  })
  유효성 검사 디테일 가능

2. 선언 후 템플릿에서 반응형 변수 {{ }}와 같은 방식으로 사용 

```

### emit
- 자식 컴포넌트가 이벤트를 발생시켜 부모로 데이터를 전달
```
1. emit
  &emit(event, ...args)
        이벤트명, 추가인자
2. event 발신
<button @click="$emit('someEvent')">클릭</button>
3. event 수신 : v-on 사용
<ParentComp @some-event="someCallback" />
```
- emit 이벤트 선언 : defineEmits()
- $emit 대신 사용할 수 있는 동등한 함수 반환
- 이벤트 발생시 추가 인자 전달 가능
