
# Don't know what this path does - nae use though!
from django.urls import path

from django.conf.urls import url
from . import views

urlpatterns = [
    url('$', views.article_list),
    # url('about/$' views.article_list),
]
