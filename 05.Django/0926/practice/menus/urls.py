from django.urls import path
from . import views

app_name = 'menus'
urlpatterns = [
    # /menus/로 요청이 왔을 때, index view 함수 실행, 이 경로의 이름이 index
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    # variable routing
    # path 함수가 호출될 때, view 함수 delete를 호출할 텐데
    # 그때, variable routing에 작성한 변수 menu_pk를 delete의 두번째 인자로 넘겨준다
    path('<int:menu_pk>/delete/', views.delete, name='delete'),

]
