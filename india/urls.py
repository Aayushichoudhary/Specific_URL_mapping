from india.views import *
from django.urls import path
app_name='win'
urlpatterns=[
    path('virat/',virat, name='virat'),
    path('shreyash/',shreyash, name='shreyash'),
]