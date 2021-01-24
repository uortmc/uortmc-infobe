from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.SystemAuth.auth_login,name='login'),
    path('signup/',views.SystemAuth.auth_signUp,name='signup')
]