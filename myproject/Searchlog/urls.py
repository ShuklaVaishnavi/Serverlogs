from django.urls import path
from . import views

urlpatterns = [
    path('Searchlog/', views.Searchlog, name='Searchlog'),
    path('',views.Homepage)
]