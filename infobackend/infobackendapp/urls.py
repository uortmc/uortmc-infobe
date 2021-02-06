from django.urls import path

from . import views

urlpatterns = [
    path('auth/login/',views.auth_login,name='login'),
    path('auth/signup/',views.auth_signup,name='signup'),
    path('authenticated/profile',views.authenticated_profile,name='profile'),
    path('authenticated/getpatients',views.authenticated_getPatient,name='getpatients'),
    path('authenticated/addpatient',views.authenticated_addPatient,name='addpatient'),
    path('authenticated/setcomment',views.authenticated_setPatientComment,name='setpatientcomment'),
    path('authenticated/getnotifications',views.authenticated_getNotifications,name='getnotification'),
    path('authenticated/addnotification',views.authenticated_addNotification,name='addnotification')
]