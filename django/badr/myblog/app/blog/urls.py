

from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("register/", views.register_request, name="register"),
    path("login/", views.login_request, name="login"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("logout", views.logout_request, name="logout")
]
