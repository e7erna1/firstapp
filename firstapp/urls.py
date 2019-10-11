from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import include, url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('article.urls')),
]
