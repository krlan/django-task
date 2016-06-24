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
]
