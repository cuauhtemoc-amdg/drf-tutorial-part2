from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    re_path('snippets/$', views.snippet_list),
    re_path('snippets/(?P<pk>[0-9]+)?$', views.snippet_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)