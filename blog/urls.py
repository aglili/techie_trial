from django.urls import path
from .views import blogView



urlpatterns = [
    path("blog",blogView,name='blog_view')
]