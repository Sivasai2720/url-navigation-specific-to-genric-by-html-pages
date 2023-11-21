from specific.views import *
from django.urls import path
app_name='specific'
urlpatterns=[
    path('madhavi/',madhavi,name='madhavi'),
    path('chaitu/',chaitu,name='chaitu'),
]