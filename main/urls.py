from django.urls import re_path, path, include
from .views import *

urlpatterns = [
    path('', index, name="home"),
    re_path(r'^api/get_members$', UserModelView.as_view())
]
