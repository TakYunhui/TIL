from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # Django가 제공해주는 user데이터가 가질 column 이외의
    # 추가 column이 필요하면 아래 필드 정의
    # 주민등록번호 = models.CharField(max_length=14)
    pass