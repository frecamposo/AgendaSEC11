from .views import *
from django.urls import re_path as url
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
   url(r'^api/contacto/$',ContactoViewSet.as_view()),   
]
urlpatterns=format_suffix_patterns(urlpatterns)