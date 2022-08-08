from django.urls import path
from . import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:id>', views.post_details, name='post_details'),
    path('post/new', views.new_post, name='new_post'),
    path('post/<int:id>/edit', views.edit_post, name='edit_post'),
]
