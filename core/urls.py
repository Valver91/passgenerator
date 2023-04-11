from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('how_work_it/', views.how_work_it, name="how_work_it"),
    path('generar/', views.home),

]