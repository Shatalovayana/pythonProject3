from django.urls import path
from rest_framework.routers import DefaultRouter

from materials.apps import MaterialsConfig
from materials.views import CourseViewSet, LessonsCreateAPIView, LessonsListAPIView, LessonsRetrieveAPIView, \
    LessonsUpdateAPIView, LessonsDestroyAPIView

app_name = MaterialsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lessons/create/', LessonsCreateAPIView.as_view(), name='lessons-create'),
    path('lessons/', LessonsListAPIView.as_view(), name='lessons-list'),
    path('lessons/<int:pk>/', LessonsRetrieveAPIView.as_view(), name='lessons-get'),
    path('lessons/update/<int:pk>/', LessonsUpdateAPIView.as_view(), name='lessons-update'),
    path('lessons/delete/<int:pk>/', LessonsDestroyAPIView.as_view(), name='lessons-delete'),
] + router.urls
