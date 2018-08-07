from rest_framework.routers import DefaultRouter
from django.urls import include, path
from . import views

app_name ='sample'

# router = DefaultRouter()
# router.register(r'posts', views.PostViewSet)

urlpatterns = [
        # path('', include(router.urls)),
        path('post/', views.PostList.as_view()),
]
