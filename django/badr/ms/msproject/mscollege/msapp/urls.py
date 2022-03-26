
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
     path('student_view_attendance/', StudentViews.student_view_attendance, name="student_view_attendance"),
     path('student_profile_update/', StudentViews.student_profile_update, name="student_profile_update"),
     path('student_view_attendance_post/', StudentViews.student_view_attendance_post, name="student_view_attendance_post"),
     path('student_view_result/', StudentViews.student_view_result, name="student_view_result"),
     path('student_feedback/', StudentViews.student_feedback, name="student_feedback"),
     path('student_feedback_save/', StudentViews.student_feedback_save, name="student_feedback_save"),
     path('student_apply_leave/', StudentViews.student_apply_leave, name="student_apply_leave"),
     path('student_apply_leave_save/', StudentViews.student_apply_leave_save, name="student_apply_leave_save")
]
