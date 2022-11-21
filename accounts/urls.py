from django.urls import path
from .views import *

app_name = "accounts"

urlpatterns = [
    path('register', register, name='register'),
    path('login', login, name='login'),
    # path('forget-password', forget-password name='forget-password'),
    path('logout', logout_user, name='logout'),
]
