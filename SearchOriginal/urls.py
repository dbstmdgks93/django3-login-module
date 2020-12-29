from django.contrib import admin
from django.urls import path, include
from SearchOriginal import views

urlpatterns = [
    path('',views.home,name='SearchOriginal'),
]