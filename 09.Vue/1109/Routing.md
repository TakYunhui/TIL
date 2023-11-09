# Routing
- 네트워크에서 경로를 선택하는 프로세스
- 웹 애플리케이션에서 다른 페이지 간의 전환과 경로 관리
## routing이 없다면
- 유저가 url을 통한 페이지 변화 감지 x
- 브라우저 뒤로 가기 기능 사용 x

### RouterView
- url에 해당하는 컴포넌트 표시
- 어디에나 배치 가능
- {{ route }} -> 객체로 데이터 저장
- JS에서 route import받아 사용


### 프로그래밍 방식 네비게이션
1. 다른 위치로 이동 : router.push()
- 이전 페이지로 뒤로 가기 가능
2. 현재 위치 바꾸기 : router.replace()
- 이전 페이지로 뒤로 가기 불가능 (히스토리에 남지 않는다)
- 로그인 상황


### Navigation Guard
- 비로그인 상황으로부터 네비게이션 보호
1. 전역 가드
- 애플리케이션 전역 (index.js)
2. 라우터 가드 
- 특정 라우트 
3. 컴포넌트 가드
- 특정 컴포넌트
```
전역 가드 
[router.beforeEach]
- to: 이동할 url 
- from: 현재 url
- 선택적 반환(return) 값: 
  false- 현재 네비게이션 취소, from url 유지
  route location- 경로 위치를 전달해 다른 위치로 redirect
  return을 안 쓰면 자동으로 to url route 객체로 이동
-> 세션, 로그인 기능

라우터 가드
[route.beforeEnter]
- route에 진입했을 때만 실행
- 매개변수, 쿼리 값이 변경될 때는 실행 x
- 다른 경로에서 탐색할 때만 실행
- component route 안쪽에 작성
- 나머지 to, from, return 값은 beforeEach와 같다

컴포넌트 가드
[onBeforeRouteLeave, onBeforeRouteUpdate]
- 현재 라우트에서 다른 라우트로 이동
- 같은 라우트 내에서 업데이트되기 전 출력
- component scripts 태그
```
