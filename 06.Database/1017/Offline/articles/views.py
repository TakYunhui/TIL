from django.shortcuts import render

# Create your views here.
def main(request):
    # BASE_DIR/articles/templates/articles/main.html
    return render(request, 'articles/main.html')


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # 물론 생성이 되지는 않는다
    else:
        # 게시글 생성을 위한 form
        form = ArticleForm()
        context = {
            'form': form
        }
    return render(request, 'articles/create.html')