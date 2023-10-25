from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('addeducation',views.addeducation,name='addeducation'), 
]