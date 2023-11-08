# Single-File Components
- Component: 재사용 가능한 코드 블록
    - UI를 독립적이고 재사용 가능한 부분으로 분할 가능
    - 앱은 중첩된 Component의 트리로 구성
- Single-File Components: 컴포넌트의 템플릿, 로직 및 스타일을 하나의 파일로 묶어낸 특수한 파일 형식(*.vue 파일)
- Vue SFC : HTML, CSS, JS 세 가지 
- play.vuejs : 단일 component 동작 확인 가능 
- 컴파일러를 통해 컴파일 된 후 빌드 되어야 함 => Vite와 같은 빌드 도구 이용

### SFC CSS - scoped
- 부모 컴포넌트의 스타일이 자식 컴포넌트로 유출되지 않음
- 단, 자식 컴포넌트의 최상위 요소는 부모와 자식의 CSS 모두의 영향을 받음

### 모든 컴포넌트에는 최상단 HTML 요소가 작성되는 것이 권장
```
<template>
    <div>
        <h1> 내용 </h1>
    </div>
</template>
```

## Vite
- 프론트엔드 개발 도구 : 빌드 도구와 개발 서버 제공
- git bash 아니고 vscode 터미널 bash 이용
```
$ npm init vue@latest
```

## Node.js
- 브라우저에서만 동작하던 JS를 서버에서 실행가능하게 함
- js로 풀스텍 가능

### vue-project 살펴보기
1. node_modules : 프로젝트의 의존성 모듈 저장, 관리, .gitignore에 작성
2. package-lock.json : npm install 명령을 통해 패키지 설치할 때 명시된 버전과 의존성 기반 설치 -> 여러 개발자가 협업할 때 일관성 주기 (requirements.txt 느낌) 
3. public : 정적 파일(소스코드 참조x, 항상 같은 이름, import 필요 x) 위치, 항상 root 절대 경로를 사용하여 참조
4. src 디렉토리 :  주요소드 코드 포함, 컴포넌트, 스타일, 라우팅 등 관리
    - assets: 이미지, 폰트, 스타일 시트 관리 => 
    - components: vue component 작성
    - App.vue: components 바깥에 위치, 최상위 component 
    - main.js: 필요한 라이브러리 import + 전역 설정
    - index.html: App.vue가 해당 페이지에 mount

### Module
- 프로그램을 구성하는 독립적 코드 블록
- 모듈 간 의존성이 깊어지면 문제 파악 힘들다 => Bundler

## Bundler
- 개발자가 신경쓰지 않아도 의존성 관리 알아서 해준다

## Virtual DOM (Vue)
- 내부 렌더링 과정
```
1. 템플릿 컴파일
2. 렌더 함수 코드 결과 반환 <=> 컴포넌트 반응형 상태 (종속성 추적 + 렌더 재실행)
3. 가상 DOM 트리 -> 실제 DOM 마운트/패치
```
- 효율성, 실시간 반응형 시스템, 추상화 
- 실제 DOM에 직접 접근 x (ex: querySelector, createElement, addEventListener)
- Vue의 ref와 LifecycleHooks와 같이 접근
- DOM element 접근 -> ref

### API 별 권장 사항
- Composition + SFC : 규모가 있는 앱의 전체 구축
- Option : 빌드 도구를 사용하지 않거나 복잡성이 낮은 프로젝트에서 사용

