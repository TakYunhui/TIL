from django.urls import path
from . import views

# app_name 구분하는 이유도 경로가 복잡해질 수록 나눠서 부르는 게 맞다
app_name = 'libraries'
urlpatterns = [
    # 사용자의 요청에 맞는 응답하기 -> 코드가 응답한다 (어떤 일을 하는 것 -> 함수)
    # Web 개발의 design pattern으로 나눠보니 M odel Template View
    path('authors/', views.authors, name='authors' )
]
