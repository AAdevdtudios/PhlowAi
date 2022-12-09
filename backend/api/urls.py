from .views import homepage, get_posts,get_single_post, update_single_post, delete_single_post
from django.urls import utils, path

urlpatterns = [
    path("/", homepage, name="api"),
    path("/posts/",get_posts, name="posts"),
    path("/posts/<int:postId>",get_single_post, name="posts"),
    path("/add/<int:postId>",update_single_post, name="update_post"),
    path("/del/<int:postId>", delete_single_post, name="delete")
]