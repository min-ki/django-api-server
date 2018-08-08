from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

app_name = 'ep03'


router = DefaultRouter()
router.register(r'post', views.PostViewSet)
router.register(r'user', views.UserViewSet)

urlpatterns = [
    # path('post/', views.PostListAPIView.as_view()),
    # path('post/<int:pk>/', views.PostDetailAPIView.as_view()),

    path('', include(router.urls)),
    # path('user/', views.user_list),
    # path('user/<int:pk>/', views.user_detail),
] 