from django.urls import path
from app2.views import *
app_name='bpk'
urlpatterns = [
    path('baby/',baby,name='baby'),
]