from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('det/<int:pk>',views.det,name='det'),
]
