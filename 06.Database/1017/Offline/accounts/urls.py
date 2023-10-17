from django.urls import path
from . import views

'''
app_name과 pattern_name은 왜 정의해주는가?
1. 하드코딩을 피하기 위해서 -> 수정사항 발생시 손으로 일일이 다 바꿔주는 일
ex) 
print('반갑습니다') * 엄청많은수 
-> 일하다보니까 반갑습니다 말고, 다른 문자를 출력해야 함 . .  .
코드 돌아다니면서 엄청 많은 print문 손으로 수정해야 함 . . .  
'''
app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
]
