from django.urls import path
from . import views

app_name = 'ep04'

urlpatterns = [
    path('post/', views.post_list),
]