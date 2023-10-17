from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('create/', views.create, name='create'),
]
