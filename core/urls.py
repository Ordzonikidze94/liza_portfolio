from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='root'),
    url(r'^news/', views.news, name='news'),
    url(r'^test/', views.test, name='test')
]
