from django.db import models

# Create your models here.
# class 명 convention - PascalCase
class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField()
    # is_published? 
    is_published  = models.BooleanField()
    # 생성일자 = DateField | YYYY-MM-DD | 2013-11-11
    created_at = models.DateField(auto_now_add=True, default='2013-11-11') 
    # 수정일자
    updated_at = models.DateTimeField(auto_now=True)
    # 사람들이 보기 좋게 문자열로 반환하는 메서드
    def __str__(self):
        return

# 설계도 만들기 -> makemigrations
# 설계도를 기반으로 실제 dp(각 테이블) 생성하기 -> migrate

'''
product1 = Product(
                name='피카츄',
                description='귀엽다',
                price=12200,
                is_published=False
)
'''