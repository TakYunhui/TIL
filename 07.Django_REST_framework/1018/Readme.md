# REST API
## API
- 애플리케이션과 프로그래밍으로 소통하는 방법
- 서로 다른 프로그램에서 요청과 응답을 받을 수 있게 해주는 방법
## Web API
- 웹 서버 또는 웹 브라우저를 위한 API
- 대표: 유튜브, 구글 맵, 네이버 파파고, 카카오 맵 ...
## REST
- Representational State Transfer
- API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
- "자원을 정의" + "자원에 대한 주소를 지정"
- 각각 API 구조 작성하는 모습이 다르니 약속을 만들어 다같이 통일해 쓰자
## REST API
- 설계 약속을 지켜서 만든 API
- 자원의 식별/행위/표현

### URI
- 자원의 식별
- 웹에서 리소스를 식별하는 문자열
- 가장 일반적인 URI == URL
#### URL
- 통합 자원 위치, 네트워스 상 리소스가 어디 있는지 알려준다
```
1. Schema (or Protocol)
- 브라우저가 리소스를 요청하는데 사용하는 규약
- URL 첫부분은 어떤 규약을 사용하는지 나타냄
- 웹은 HTTP(S)를 사용

2. Domain Name
- 요청 중인 웹 서버를 나타낸다
- 사람이 보기 쉽게 만든 name

3. Port
- 웹 서버의 리소스에 접근하는데 사용되는 기술적인 문(Gate)
- HTTP:80, HTTPS:443
- 표준 포트는 생략 가능

4. Path
- 웹 서버의 리소스 경로
- 과거에는 실제 파일이 위치한 물리적 위치를 나타냈으나,
- 현재는 실제 위치가 아닌 추상화된 형태의 구조를 표현

5. Parameters
- 웹 서버에 제공되는 추가적인 데이터

6. Anchor
- 북마크 
```

#### HTTP Request Methods
- 자원에 대한 행위
```
1. GET: 데이터 조회(R)
2. POST: 데이터 생성(C)
3. PUT: 데이터 수정(U)
4. DELETE: 데이터 삭제(D)
```
- 5개의 응답 그룹

#### JSON 타입
- REST API는 html이 아니라 JSON타입 응답 권장 
- Django가 풀스텍 -> front-end & back_end 분리


# Serialization 
- 여러 시스템에서 활용하기 위해 데이터 구조나 객체 상태를 나중에 재구성할 수 있는 포맷으로 변환하는 과정
- 어떠한 언어나 환경에서도 적합하게 사용 가능하게 함

## DRF with single model
- 이전 view는 html에 출력되도록 페이지와 함께 응답했으나 이제 json데이터로 serialization하여 페이지 없이 응답 가능 
### api_view decorator
- 기본적으로 GET 메소드
- DRF view함수에서 필수로 작성