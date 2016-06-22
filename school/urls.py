from rest_framework import routers
from django.conf.urls import url, include
from . import views

router = routers.DefaultRouter()
router.register(r'school', views.SchoolViewSet)
router.register(r'class', views.ClassroomViewSet)
router.register(r'student', views.StudentViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^school/(?P<pk>[0-9]+)/$', views.school, name='school'),
    url(r'^class/(?P<pk>[0-9]+)/$', views.classroom, name='class'),
]
