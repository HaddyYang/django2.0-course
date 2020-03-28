from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('user_info/', views.user_info, name='user_info'),
    path('change_nickname/', views.change_nickname, name='change_nickname'),
    path('bind_email/', views.bind_email, name='bind_email'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('change_password/', views.change_password, name='change_password'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('login_by_qq', views.login_by_qq, name='login_by_qq'),  # zqyhdm.com/user/login_by_qq
    path('bind_qq', views.bind_qq, name='bind_qq'),
    path('create_user_by_qq', views.create_user_by_qq, name='create_user_by_qq'),
]