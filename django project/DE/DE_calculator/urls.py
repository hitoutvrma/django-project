from django.contrib import admin
from django.urls import path
from DE_calculator import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addition',views.addition,name='addition'),
    path('subtraction',views.subtraction,name='subtraction'),
    path('kmap',views.kmap,name='kmap'),
    path('bitham',views.bitham,name='bitham'),
    path('queenmcclusky',views.queenmcclusky,name='queenmcclusky'),
    path('bitogrey',views.bitogrey,name='bitogrey')
]
 
