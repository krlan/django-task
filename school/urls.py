from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug_school>[\w-]+)/$', views.school, name='school'),
    url(r'^(?P<slug_school>[\w-]+)/(?P<slug_class>[\w-]+)/$', views.classroom, name='classroom'),
    url(r'^(?P<slug_school>[\w-]+)/(?P<slug_class>[\w-]+)/(?P<slug>[\w-]+)/$', views.student, name='student'),
]
