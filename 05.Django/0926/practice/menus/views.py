from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect
from .models import Menu
from .forms import MenuForm

# Create your views here.
def index(request):
    menus = Menu.objects.all()
    context = {
        'menus': menus,
    }
    return render(request, 'menus/index.html', context)


def detail(request, pk):
    menu = Menu.objects.get(pk=pk)
    context = {
        'menu': menu,
    }
    return render(request, 'menus/detail.html', context)


def new(request):
    
    # POST 방식 요청
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            # POST 요청에 대한 처리는 위에서 마쳤음. 
            return redirect('menus:index')
    else:
        form = MenuForm()
    # 파이썬에서 정의한 데이터를 html에서 DTL 형태로 쓸 수 있도록
    # render 함수가 html을 잘 렌더링할 수 있도록
    context = {
        'form': form,
    }
    return render(request, 'menus/new.html', context)


def create(request):
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save()
            return redirect('menus:detail', menu.pk)
        
    else:
        form = MenuForm()
    context = {
        'form': form,
    }

    return render(request, 'menus/create.html', context) 

@require_POST
def delete(request, menu_pk):
    # get method => 키워드 인자 = value
    menu = Menu.objects.get(pk=menu_pk)
    menu.delete()
    return redirect('menus:index')