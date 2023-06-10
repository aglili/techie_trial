from django.urls import path
from . import views


urlpatterns = [
    path("blogs/public",views.publicBlog,name='all_posts'),
    path("blog",views.createBlog,name='create_blog'),
    path("blog/all",views.getUserBlog,name='get_user_posts'),
    path("blog/update",views.updateUserBlog,name='update_blog'),
    path("blog/delete",views.deleteBlog,name='delete_blog')
]