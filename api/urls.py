from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api.views import PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register('post', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
