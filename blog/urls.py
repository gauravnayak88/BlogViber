from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.index, name='blog-index'),
    path('post_detail/<int:pk>', views.post_detail, name='blog-post-detail'),
    path('comment/<int:cid>/delete', views.comment_delete, name='comment-delete'),
    path('comment/<int:cid>/edit', views.comment_edit, name='comment-edit'),
    path('post_edit/<int:pk>', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>', views.post_delete, name='blog-post-delete'),
]
