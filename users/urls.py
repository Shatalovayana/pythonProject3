from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UsersViewSet

app_name = UsersConfig.name

router = DefaultRouter()
router.register(r'course', UsersViewSet, basename='course')

urlpatterns = [

] + router.urls
