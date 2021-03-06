from . import views

from django.urls import path

app_name = "blog"

urlpatterns = [

    path('', views.PostList.as_view(), name='home'),

    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path("logout", views.logout_request, name="logout"),
    path("member", views.member, name="member"),
    path("password_reset", views.password_reset_request, name="password_reset"),


]
