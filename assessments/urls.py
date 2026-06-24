from rest_framework.routers import DefaultRouter
from .views import AdminCreateStudentViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'admin-create-students', AdminCreateStudentViewSet, basename='admin-create-students')

urlpatterns = [
    path('', include(router.urls)),
]
