
from django.urls import path
from  . import views

urlpatterns = [
    path('iris', views.home),
    path('iris/result', views.result,name='predict')
    
]
