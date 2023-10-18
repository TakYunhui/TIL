from django.shortcuts import render,redirect


from .models import Article
from .forms import ArticleForm

# Create your views here.
def main(request):
    # 게시글 전체 정보 조회
    # Model.manager.querySetAPI
    # SELECT * FROM articles_article;
    # articles = Article.objects.all()

    # SELECT * FROM articles_article ORDER BY pk DESC;
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles
    }
    # BASE_DIR/articles/templates/articles/main.html
    return render(request, 'articles/main.html', context)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 물론 생성이 되지는 않는다
            # form.save() 메서드는 생성된 데이터 인스턴스 반환
            # db의 테이블에 생성될 값 INSERT INTO
            # 이때, article이 가지고 있을 user_id를 안 넣고 생성하려면 문제 발생

            # 그럼 article에 user 정보(요청 유저)를 담아야 하니
            # article 생성은 하나 db에 보내지는 않는다
            article = form.save(commit=False)
            # 생성된 article 객체의 user 속성에 요청보낸 request.user 정보만 담기
            # 담은 것은 python의 article 변수의 값에만 할당한 것
            # db에 반영
            article.user = request.user
            article.save()
            return redirect('main')
    else:
        # 게시글 생성을 위한 form
        form = ArticleForm()
        context = {
            'form': form
        }
    return render(request, 'articles/create.html')