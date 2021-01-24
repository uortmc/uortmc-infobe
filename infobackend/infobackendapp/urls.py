from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.SystemAuth.auth_login,name='login')
]