
# Don't know what this path does - nae use though!
from django.urls import path

from django.contrib import admin
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^articles/', include('articles.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
]
