from . import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
app_name = "blog"

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path("login/", views.login_request, name="login"),
    path("register/", views.register_request, name="register"),
    path("logout/", views.logout_request, name= "logout"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='blog/password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(template_name="blog/password/password_reset_confirm.html",
        success_url=reverse_lazy('blog:password_reset_complete')),
        name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='blog/password/password_reset_complete.html'), name='password_reset_complete'),      
    path("password_reset", views.password_reset_request, name="password_reset")

]
