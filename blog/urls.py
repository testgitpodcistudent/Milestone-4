from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_blog, name="view_blog"),
    path("create_post/", views.create_post, name="create_post"),
    path("<int:post_id>", views.post_page, name="post_page"),
    path("delete_post/<int:post_id>/", views.delete_post, name="delete_post"),
    path("edit/<int:post_id>/", views.edit_post, name="edit_post"),
]
