from django.urls import path 
from . import views
from django.conf.urls import url
# from django.views.generic.base import TemplateView
from fallguys.views import todo

app_name = 'fallguys'

urlpatterns = [ 
    path('', todo.as_view(), name='todo'),
]