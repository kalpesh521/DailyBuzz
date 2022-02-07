from django.urls import path
from newsapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.home, name='home'),
    path('', views.about, name='about'),
    path('', views.contact, name='contact'),
]