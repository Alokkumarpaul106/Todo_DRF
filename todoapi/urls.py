from .views import TaskViewSet,CategoryViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .import views
from django.urls import path,include
router = DefaultRouter()
router.register(r'task', TaskViewSet, basename='task')
router.register(r'category',CategoryViewSet,basename='category')


urlpatterns = [
    path('api-token-auth/', obtain_auth_token),  #used for api token
    path('', include(router.urls)),
    
]
