from django.urls import path, include
from . import views
urlpatterns = [
    #跳转页面
    path('order/', views.testone),
    #获得表单信息的url
    path('getproduct/', views.get_product_json),
    #模糊搜索获取所有产品名的URL
    path('get_product_name/', views.get_product_name),
    #模糊搜索获取所有仪器名的URL
    path('get_instrument_name/', views.get_instrument_name),

]