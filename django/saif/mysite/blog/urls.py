from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name= "logout"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
