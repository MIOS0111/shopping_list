from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name="main_page"),
    path("logout/", views.logout_request, name="logout"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("my/", views.PostList.as_view(), name="my"),
    path("contacts/", views.contacts, name="contacts"),
    path("create_post/", views.create_post, name="create_post"),
    path("delete_post/<int:pk>/", views.delete_post, name="delete_post"),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('feedback_list/', views.feedback_list, name='feedback_list'),
    path('register/', views.register, name='register')
]