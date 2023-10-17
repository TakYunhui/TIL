## 팔로우 기능
```py
# accounts > urls.py
# 유저네임을 변수로 받는 url path 추가
    path('profile/<str:username>/', views.profile, name='profile'),
# profile/을 앞에 써주어서 뒤에 오는 문자열들을 볼 수 있게 해준다
# 안 써주면 문자열을 모두 <username>으로 봐서 실행 x
# 다른 해결법으로는 path 위치 조정이 있다 (CASCADE하기 때문)
```
- 자기 자신과의 M:N 관계
- 두 테이블을 각각 참조하는 중개 테이블 생성

### .exists()
- QuerySet에 결과가 포함되어있으면 True 반환, 포함되어 있지 않으면 False 반환
- 큰 QuerySet에 있는 특정 객체 검색에 유용

### Fixtures
- Django가 DB 초기 데이터를 만들 때 사용하는 데이터 형식
- dumpdata : 현재 데이터 추출 (생성)
- loaddata : 데이터 입력 (로드)
- Fixtures 파일 기본 경로 : app 폴더의 fixtures 
- app_name/fixtures/
- load를 하나씩 실행하면 모델 관계에 따라(FK) load순서가 중요해질 수 있다
- 그냥 한번에 하면 편하고 상관 없다
```
python manage.py dumpdata --indent 4 > data.json
python manage.py dumpdata --indent 4 articles.article articles.comment accounts.user > data.json
```
- Fixtures 파일을 직접 만들지말고 반드시 dumpdata로 추가

### Improve query
- 같은 결과를 얻기 위해 db를 점차 줄여가며 조회
#### annotate
- SQL의 GROUP BY 쿼리 사용
- 매 게시물마다 댓글 COUNT -> views에서 조회할 때 애초에 가져온다
#### prefetch_related
- 위와 유사하나 모델 관계 유의
