from django.urls import path
from . import views

urlpatterns = [
    path('default/', views.index, name='index'),
    path('', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),
    path('add-post/', views.add_post, name="add_post"),
    path('post-detail/<slug>', views.post_detail, name="post_detail"),
    path('see-post/', views.see_post, name="see_post"),
    path('post-delete/<id>', views.post_delete, name="post_delete"),
    path('add-comment/<slug>/', views.add_comment, name="add_comment"),
    path('post-update/<slug>/', views.post_update, name="post_update"),
    path('logout-view/', views.logout_view, name="logout_view"),
    path('verify/<token>/', views.verify, name="verify"),
]
