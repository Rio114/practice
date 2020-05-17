from django.urls import path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from . import views, forms


app_name = 'srgan'
urlpatterns = [
    # path('', views.IndexView.as_view(), name='index'),
    # path('send/', views.SendView.as_view(), name='send'),
    url(r'^$', views.form, name = 'form'),
    url(r'^complete/', views.complete, name = 'complete'),
]
