from django.urls import path

from . import views

urlpatterns = [
    path('auth/login/',views.auth_login,name='login'),
    path('auth/signup/',views.auth_signup,name='signup'),
    path('authenticated/profile',views.authenticated_profile,name='signup')
]