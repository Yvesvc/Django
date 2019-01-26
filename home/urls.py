from django.shortcuts import render
from django.urls import path, include
from . import views

urlpatterns = [path('', views.product_url, name = 'product_url')]
