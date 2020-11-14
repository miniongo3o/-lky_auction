from django.urls import path
from . import views

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('bid/', views.do_bid, name='do_bid'),
]