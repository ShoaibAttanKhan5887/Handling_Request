from django.contrib import admin
from django.urls import path
from Home import views # You have to include this in every project that you do
urlpatterns = [
    path("",views.index,name='home'),
    path("check_request",views.check_request,name='check_request'),
]