
from django.urls import path
from . import StudentViews
from . import views

urlpatterns  = [
    path('',views.home,name="home"),
    path('login/',views.loginUser,name="login"),
    path('doLogin',views.doLogin,name="doLogin"),
    path('contact',views.contact,name="contact"),
    path('registration',views.registration,name="registration"),
    path('doRegistration',views.doRegistration,name="doRegistration"),
    path('logout_user',views.logoutUser,name="logout_user"),

    # URLS for Student
     path('student_home/', StudentViews.student_home, name="student_home"),
     path('student_profile/', StudentViews.student_profile, name="student_profile"),
     path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance")
]
