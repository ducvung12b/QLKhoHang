from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.dshanghoa, name='dshanghoa'),
    path('themhanghoa/', views.themhanghoa, name='themhanghoa'),
    path('dshanghoa/', views.dshanghoa, name='dshanghoa'),
    path('suahanghoa/<int:id_hang_hoa>/', views.suahanghoa, name='suahanghoa'),
]
