from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # 제목, 내용, 작성 시간, 수정 시간
    # models 라는 모듈에 다양한 필드가 정의됨
    # 각 필드들은 db에 생성될 table의 컬럼별 데이터 타입을 적절하게 정의
        # database_sometable
        # | pk  |    title    |  content  |   created_at . . . 
        # | INT | VARCHAR(100)|    TEXT   |   DATETIME
    title = models.CharField(max_length=100)  
    content  = models.TextField()
    # 작성 시간 : 사용자가 직접 입력하지 않는다 
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정 시간 : 사용자가 직접 입력하지 않는다  
    updated_at  = models.DateTimeField(auto_now=True)
    # User와의 관계
    # article.user (작성자 정보)
    # == models.ForeignKey('accounts.User')
    # 참조하고 있는 유저가 삭제되면 그 게시물 자체도 같이 삭제되게 한다 (회원 탈퇴시, 해당 유저 게시글까지 삭제)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # User와의 관계 - M:N
    # 좋아요 기능 구현을 위한 관계
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

    # related_name : 
    # a1(게시글 하나)는 직접적으로 like_user를 가지지만, 
    # user1(게시글과 M:N 관계를 맺은 유저)는 class에 해당 관계에 대한 변수 및 속성을 정의한 적 없음 
        # 그래서 django가 manager를 만들어주며 related manager -> user1.article_set.querySET
        # related manager 이름 작성 규칙 : 관계 맺고 있는 class의 소문자_set 
    # related manager는 M:N만 있는 게 아니다 (M:N은 서로가 서로를 1:N하고 있는 것)

# 중개 모델을 사용해 M:N을 표현할 수도 있다
# 근데 User -> LikeSystem-> Article 단계를 거쳐서 찾아야 한다 . .  .
# 너무너무귀찮다 
    # articles = User.likesystem_set.all()
    # for article in articles:
    #   article.title
# class LikeSystem(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)

# 댓글
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)