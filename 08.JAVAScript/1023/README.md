# JS
## 실행 환경 종류
1. html body script 태그 + alt B로 확인 웹 실행하여 확인 가능
2. js 확장자 파일
3. 브라우저 내 콘솔

## DOM
- 웹 페이지를 객체 모델로 바라보기 
-> 객체로 보는 이유? 동적인 기능을 추가하려면 문서를 조작해야 한다
=> 요소를 '선택'할 수 있어야 한다 

## DOM Tree
- 객체 간 상속 구조 존재
- 'document' : 웹 페이지 console 왼쪽에 보이는 전체화면 모든 것
### 선택 메서드
1. 단일 선택: document.querySelector()
- querySelector(selector) : 제공한 선택자와 일치하는 요소 1개 선택, 여러 개면 첫번째 객체 반환 (없다면 null)
2. 다중 선택: document.querySelectorAll()
- querySelectorAll(selector): 제공한 선택자와 일치하는 여러 요소를 선택 -> NodeList 반환
- NodeList: 대괄호([ ])로 감싸져 있어 배열처럼 사용 가능

### DOM 선택
- F12 구문 오른쪽 마우스 클릭 > COPY >> Selector등 복사 가능
- 복사한 것을 querySelctor에 바로 넣으면 된다

### DOM 조작 
1.  속성 조작
  (1) 클래스 속성 : <h1 class="">
- classList 속성값에 접근
- 유사배열 형태로 반환 3가지 메서드
```
add(): 지정한 클래스 값 추가
remove(): 제거
toggle(): 존재하면 제거 false, 존재하지 않으면 클래스 추가 true 반환
```
  (2) 일반 속성 : <a href="">
```
getAttribute(): 해당 요소에 지정된 값 조회(반환)
setAttribute(): 지정된 요소의 속성 값 설정, 속성이 이미 있으면 기존 값 갱신 (없으면 새 속성과 값 추가)
removeAttribute(): 속성 제거
```

### HTML 콘텐츠 조작
- textContent: 태그와 태그 사이 값 조작

### DOM 요소 조작 메서드 
- createElement(tagName) : 작성한 tagName의 HTML 요소 생성하여 반환
- Node.appendChild() : 한 Node를 특정 부모 Node 자식 NodeList 중 마지막 자식으로 삽입, 추가된 Node 객체 반환
- Node.removeChild() : DOM에서 자식 Node 제거, 제거된 Node 반환
