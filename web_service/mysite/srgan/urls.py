from django.urls import path
from . import views

app_name = 'srgan'
urlpatterns = [
    path('', views.index, name='index'),
]
