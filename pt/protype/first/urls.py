from django.urls import path, include
from .import  views

app_name = 'first'
urlpatterns = [
    path('', views.mainPage, name = 'MainPage'),
    path('login/', views.logIn, name = 'Login'),
    path('logout/', views.logOut, name = 'Logout'),
    path('register/', views.regist, name = 'Register'),
    path('pic_upload/', views.pic_upload, name='Pic_upload'),
    path('pic_show/', views.pic_show, name='Pic_show'),
]
