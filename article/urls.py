from django.conf.urls import url
from article import views

urlpatterns = [
    url(r'^articles/all/$', views.articles),
    url(r'^articles/get/(?P<article_id>\d+)/$', views.article),
    url(r'^$', views.articles),

]
