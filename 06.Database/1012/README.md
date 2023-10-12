# N: 1 관계
## User 
#### User가 Article과 Comment와 어떤 관계를 가지는지?
- 대체가 되어있는 User Model을 쓰는 상황에서 어떻게 이루어지는지?

## Article(N) - User(1)
- 0 개 이상의 게시글은 1명의 회원에 의해 작성 가능하다 
- User를 참조하는 FK가 Article에 추가
```py
# User model 간접 참조
# articles > models.py
from django.conf import settings
class Article(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
```
- django 에서 User model을 직접 참조하는 것을 권장하지 않는다
- 따라서 settings 사용 (또는 get_user_model()도 같은 동작)
- 하지만 settings을 사용하는 이유? 
  - get_user_model : User Object(객체) 반환
  - settings.AUTH_USER_MODEL : accounts.User(문자열) 반환
    - 아직 User 객체가 django에 존재하지 않는 순간, 객체를 반환하려고 하면 문제가 발생 가능하다
    - 예를 들면 FK로 쓰려는데 클래스 순서가 맞지 않을때도 문자열로 이용하면 된다 (libraries.Review)
- User만 setting.py에 AUTH_USER_MODEL로 빼주는 이유? 
    - django에 user_id 같은 부분에 AUTH_USER_MODEL이 쓰여있다, 변수 따로 수정 안 해두면 기본 값(auth.User)으로 테이블 만듦
```
[Migration 오류]
python manage.py makemigrations
python manage.py migrate

-> It is impossible to add a non-nullable filed 'user' ... 
```
- migrate하려면 발생하는 오류?
- 이미 게시글이 작성되어 테이블이 있는데 null한 user 정보를 새로 추가하려 하기에 발생한다
- default에 임의의 정수값 1을 넣어서 해결 (하란 대로 하면 됨)
- 또는 DB를 초기화하고 새로운 migrate 진행
- 외래키는 테이블 뒷쪽부터 작성이 된다
```
[User 만들기]
사이트에 회원가입하고 로그인 진행

[게시글 생성 with 새로운 모델 관계]
CREATE에 User 정보 필드 생김... => 사용자가 user 정보 선택? 절대 안 됨!
article form에서 보이는 것이기 때문에 
exclude = ('user',) 로 가려준다. 
```
- 하지만 가려준 것 뿐, 문제가 해결된 것은 아님!
- 해결하기 위해서는?
```py
# articles > views.py
# creat 함수
  if form.is_valid():
    article = form.save(commit=False)
    article.user = request.user
    form.save()
```
- commit=False! 아주 중요함
- 현재 유저 정보는 request에서 user란 객체 가져온다
- model 인 article이 아니라 form instance의 save method 사용
- 이유? form에서 내부적인 보안이 더 있는 save이기 때문이다
```py
# update 함수
  # 현재 user가 게시글의 user와 같다면 수정 가능
  if request.user == article.user:
  else:
    return redirect('articles:index')
```
- 남의 글을 수정하지 못 하게 한다
- 자기 자신의 글만 수정 가능 
- 수정할 때는 commit=False 왜 안 하나요? 
- 이미 유저 정보가 들어가 있기에 user 정보를 넣어줄 필요가 없다! 
```html
  {% if request.user == article.user %}
    <a href="{% url "articles:update" article.pk %}">UPDATE</a>
    <form action="{% url "articles:delete" article.pk %}" method="POST">
      {% csrf_token %}
      <input type="submit" value="삭제">
    </form>
  {% endif %}
```
- 애초에 본인이 쓴 글에만 수정, 삭제 버튼이 보이게 처리
```py
# delete 함수
    if request.user == article.user:
        article.delete()
```
- 요청하는 사람과 작성자의 비교로 삭제 여부 판단



## Comment(N) - User(1)
- 0 개 이상의 댓글은 1명의 회원에 의해 작성 가능하다
- User를 참조하는 FK가 Article에 추가
- 두 개에 종속됨 : 어디(article)에 작성했는지, 누가(user) 작성했는지 
```py
# articles > views.py
# comment_create 함수
  if comment_form.is_valid():
    . . . 
    comment.user = request.user # 현재 로그인된 유저 정보 넣어주기
```
- 댓글 입력하고 발생하는 Intergery 오류 (필요한 데이터가 없다) 해결 
```
[댓글 내용 앞에 유저 출력]
html에서 {{comment.user}} - {{comment.content}}
```
```
[댓글 삭제]
작성자와 request.user가 같다면 삭제하도록 함
        {% if request.user == comment.user %}
          <form action="{% url "articles:comments_delete" article.pk comment.pk %}" method="POST">
            {% csrf_token %}
            <input type="submit" value="삭제">
          </form>
        {% endif %}
```
- @login_required : 인증된 사용자만 댓글 작성 및 삭제 
- 데코레이터는 이어서 쓸 수 있다, 순서가 중요해진다

###### 참고 : 스타일 가이드
[ import 순서 ] 
1. python standard library
2. python 외부 설치 library
3. django 내장 모듈
4. django local 
```
$ isort . 
```
- import 정렬 
[ template 스타일 ]
DO : {{ foo }} 중괄호 사이에 공백
[ View 스타일 ]
첫번째 인자로 반드시 request를 받는다 (다르게 사용 x)
[ Model 스타일 ]
- 모델 클래스 필드 이름은 전부 다 소문자 + 공백은 언더바로 작성
- 카멜스타일 사용 x
[ Class meta ]
- class Meta의 위치는 필드를 선언하는 곳 아래쪽 
1. 데이터베이스 필드
2. 커스텀 속성
3. 클래스 메타
4. def __str__()
5. def save()
6. def get_absolute_url()

###### 참고 : 데이터 모델링
- 데이터베이스 시스템을 시각적으로 표현하는 프로세스
- ERD : 다이어그램을 사용하여 데이터베이스의 Entity 간 관계를 나타내는 방법
```
 Entity : 테이블
 Attribute : 필드
 Relation : PK, FK
```
- Cardinality(기수) 
- Optionality(선택 가능성) : 필수/선택?
