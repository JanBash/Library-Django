from django.urls import path

from .views import posts, post_detail

urlpatterns = [
    path('', posts),
    path('<int:pk>/', post_detail),
]