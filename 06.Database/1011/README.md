# Databse

> SSAFY 10기 Databse 과정 라이브 강의 코드

| 진행일 | 주제                    |
| ------ | ----------------------- |
| 10/10  | SQL  |
| 10/11  | Many to one relationships 1 |
| 10/12 | Many to one relationships 2 |
| 10/16 | Many to many relationships 1 |
| 10/17 | Many to many relationships 2 |

## N : 1 관계
- Mant to one relationships 
- 한 테이블의 0개 이상의 레코드가 다른 테이블의 레코드 한 개와 관련된 관계
- (ex) 댓글과 게시글의 관계 : 0 개 이상의 댓글은 1개의 게시글에 작성될 수 있다
- n : 1 관계에서 foreign key는 n 쪽이 가지게 된다 

### 댓글 모델 구현
1. articles app에 댓글 모델 정의
```python
article = models.ForeignKey(Article, on_delete=models.CASCADE)
``` 
- 외래키 필드는 2개의 인자를 필수로 가짐
- to : 참조할 모델 클래스 이름
- on_delete : 외래 키가 참조하는 키(1)가 사라졌을 때, 외래 키를 가진 객체(N)을 어떻게 처리할 지 결정
- on_delete = models.CASCADE
- 부모 객체(참조 객체)가 삭제됐을 때, 이를 참조하는 객체도 삭제 

2. ORM 에 의해서 sql이 어떻게 해석되는지 확인
```bash
python manage.py sqlmigrate articles 0002
```
```
BEGIN;
--
-- Create model Comment
--
CREATE TABLE "articles_comment" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content" varchar(200) NOT NULL, "created_at" datetime NOT NULL, "updated_at" datetime NOT NULL, "article_id" bigint NOT NULL REFERENCES "articles_article" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE INDEX "articles_comment_article_id_59ff1409" ON "articles_comment" ("article_id");
COMMIT;
```

3. 실제 테이블 확인
- DB 열기
- article_id 가 아니라 그냥 id로 만들어야 한다! 
- python manage.py shell_plus 에서 
- article, comment instance 만들기 
- comment 생성시 error? IntegrityError: NOT NULL constraint failed: articles_comment.article_id
- articles_comment.article_id 댓글 테이블의 외래 키 article_id가 누락되었기에 값을 저장할 수 없다 (제약 조건을 통과 못 했음!)
- comment.article = article 와 같이 통째로 넣으면 테이블에 pk가 알아서 저장된다
- 저장 후 제대로 만들어졌는지 comment.pk 확인 + 테이블 확인

### 관계 모델 참조
- 역참조: N:1 관계에서 1에서 N을 참조하거나 조회 
- 게시글에 작성된 모든 댓글 조회
- N은 외래키를 가져 물리적으로 참조 가능하나 1은 N에 대한 참조 방법이 존재하지 않아 별도의 역참조 이름이 필요
```python
article.comment_set.all()
```
- 모델인스턴스.역참조이름.QuerySet API
```
[related manager] 
- 역참조 이름
- queryset api를 사용할 수 있게 함 (like objects manager)
- 상대방 이름에 따라 이름이 달라질 수 있다

[이름 규칙]
- 참조하는 모델명_set
- 해당 댓글의 게시글(comment > article) : comment.article
- 게시글의 댓글 목록 (article > comment) : article.commet_set.all()
- 이때 생성한 쿼리는 새 변수에 지정하여 활용 

[쿼리셋을 이용하여 댓글 조회]
comments = article.comment_set.all()
for comment in comments:
  print(comment.content)
```

### 댓글 CREATE 구현
1. 사용자 댓글 입력을 받을 모델Form 정의
- articles forms.py 
- CommentForm() 생성 
- 해당 게시글에 바로 comment 남기도록 fields = ('content',) 로 내용만 보이게 한다 
2. url, views, html 작업 
- 게시글 조회 후 폼에서 받은 데이터 출력
- article이 등장할 타이밍 잡기
```
save(commit=False)
```
- DB에 저장하지 않고 인스턴스만 반환

### 댓글 READ 구현
#### 역참조
1. 게시글의 댓글 가져오기 
- comments = article.comment_set.all()
- 이때, Comments.objects.all()과 혼동 주의, 이는 게시글 상관 없이 모든 댓글 목록을 가져온다
2. html에서 for문을 통해 comment 출력 

### 댓글 DELETE 구현
1. 댓글 삭제 URL 작성
- article_pk 이용하면 일관성 있다
- comment로만으로도 구현은 가능하다 
