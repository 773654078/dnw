from django.urls import path, include
from . import views
urlpatterns = [
    #跳转页面
    path('create/', views.testone),

]