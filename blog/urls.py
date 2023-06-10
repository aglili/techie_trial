from django.urls import path
from . import views


urlpatterns = [
    path("blog",views.createBlog,name='create_blog'),
    path("blog/all",views.getUserBlog,name='user_posts')
]