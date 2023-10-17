# Django란,
- Web FrameWork

### Web Service(project) 구축하려면,
1. 가상환경
- 내 프로젝트만을 위한 패키지들의 버전을 관리
```bash
$ python -m venv venv
$ pip install package 
$ pip freeze > requirements.txt
```

2. 버전관리
- `.gitignore` 라는 gitignore 확장자 파일에 git으로 관리하지 않을 파일 목록을 작성하여 관리
```bash
$ git init
```

### Django 프로젝트 생성
```bash
# $ python file_path
# django야 플젝 만들거라 플젝 이름은 이거고 여기 만들기다
$ django-admin startproject { pjt_name } { pjt_path }
$ python manage.py runserver
```

### APP 생성 및 등록과 설정
> 주의사항 : app 생성 후 등록 
> 생성 전에 등록할 수 없다 
```bash
$ python manage.py startapp articles
$ python manage.py startapp accounts
```

```py
# crud/settings.py
INSTALLED_APPS = [
  ...
  'articles',
  'accounts',
]
```

### 모델 정의
- 각 App의 models.pt 참고
```bash
# 설계도 작성 명령어
# model.py에 작성한 class 기반으로 적절한 table이 되도록 각종 데이터타입 설정 
$ python manage.py makemigrations
# 설계도 기반 table 생성
$ python manage.py migrate
```

### 화면 구성을 위한 준비 (base.html)
- 만드는 이유 : 한 서비스 내의 화면 구성을 동일하게 작성
- 매번 똑같은 코드를 반복해서 작성하지 않도록 하기 위해서 base.html을 작성해 상속받아 사용 
- base.html 작성 위치? (사용 용도에 따라 달라짐)
1. articles app의 화면 구성만을 위한 base는 articles app 폴더에서
2. 모든 app이 공통으로 사용할 것이라면, 최상위 루트에 작성
  - django는 기본적으로 app폴더만 탐색해 파일을 찾는다
  - 다른 루트에서 만든 파일을 찾을 수 있게 하려면, settings.py에 작성 필수

### 기능 구현
1. 특정 경로로 요청이 들어온다
2. 해당 요청에 대한 적절한 대응 (view 함수)
  - DB로부터 CRUD를 행할 수도 있고,
  - 특정한 Template를 반환할 수도 있고, . . .