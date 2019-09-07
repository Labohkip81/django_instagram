from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('<int:user_pk>/', UserDetailView.as_view(), name='details'),
    path('<int:user_pk>/edit/', UserEditView.as_view(), name='edit'),
    path('<int:user_pk>/password_change/', UserSubscribeView.as_view(), name='subscribe'),
    path('<int:user_pk>/subscribe/', UserPasswordChangeView.as_view(), name='password_change'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('register/', account_register_view, name='register'),
    path('login/', account_login_view, name='login'),
]
