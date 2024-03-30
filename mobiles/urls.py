from django.urls import path
from mobiles.views import *
app_name='anything'
urlpatterns=[
    path('redmi/',redmi,name='redmi'),
]