from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # 사용자가 요청 보낸 method에 따라 조건 분기처리해 서로 다른 행동
    if request.method == 'POST': # 데이터 생성
        # 사용자가 보낸 데이터로 User 만들기
        '''
        user = accounts.User()
        user.username = request.POST.get('username')
        user.password = request.POST.get('password')
        user.save()
        '''
        # 유저 생성을 위해 필요한 각 필드에 대한 정보 -> User 모델에 있음
        # User 모델에 대한 정보는 ModelForm에 있음
        # form 인스턴스 만들때 request.POST에 있는 데이터를 포함해서 만들면?
        form = CustomUserCreationForm(request.POST)
        if form.is_valid(): # 유효성 검사
            form.save() # 저장 -> DB 반영
            # redirect의 첫번째 인자로 작성할 내용?
                # 사용자를 어디로 보낼 것인지 (어떤 경로로 요청한 것으로 취급할 것인지)
                # redirect('app_name:pattern_name')
                # redirect('pattern_name')
                # redirect('url')
            # redirect 함수가 하는 일?
                # 작성된 to 위치로 GET요청 실행
            return redirect('main')
    else: # 그외의 경우 회원가입 페이지 보여주기 
        # 회원가입 버튼 클릭 -> 회원가입할 수 있는 페이지 보여줘
        # 회원가입할 수 있는 페이지를 사용자에게 반환 
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    # render 함수 : html 파일 렌더링
    # BASE_DIR/app/templates/accounts/signup.html
    # C:\Users\SSAFY\Desktop\Lectures\-6_database\05... - 윈도우식 표기, 파이썬에서 백슬래시는 escape문자임을 주의
    return render(request, 'accounts/signup.html', context)


def login(request):
    if request.method == 'POST':
        # 사용자가 보내준 데이터로 form 생성
        form = AuthenticationForm(request, request.POST)
        # 인증 이라는 행위는 . . . -> DB에 있는 username과 password와
        # 사용자가 보내준 username과 password가 일치하면 된다
        # DB를 생성하거나 하는 행위는 없다 
        if form.is_valid():
            # 유효성 검사가 문제 없으면 '로그인' 행위를 한다
            # 로그인이란, 현재 사용자가 보내준 데이터를 기반으로 특정 유저를 찾는다
            # 그 특정 유저에 대한 정보를 암호화해서 사용자에게 돌려준다
            # 사용자는 다음 요청부터는 넘겨받았던 데이터를 함께 동봉해서 보낸다
            # 서버는 그렇게 사용자가 보내준 암호화된 데이터를 토대로 유저를 인식한다
            auth_login(request, form.get_user())
            return redirect('main')

    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout(request):
    # 세션에서 연결된 user 정보 제거
    if request.method == 'POST':
        # request에는 현재 로그인된 유저 정보가 포함되어 있다
        auth_logout(request)

    return redirect('accounts:login')