from loki.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('loke/',loke,name='loke')
    ]