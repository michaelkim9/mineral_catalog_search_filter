from django.urls import re_path

from . import views

app_name = 'minerals'

urlpatterns = [
    re_path(r'(?P<pk>\d+)/$', views.mineral_detail, name='detail')
]
