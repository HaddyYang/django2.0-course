from django.urls import path
from . import views


urlpatterns = [
    path('like_change', views.like_change, name='like_change')
]