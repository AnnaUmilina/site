from django.urls import path
from user import views

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login-user/', views.login_user, name='login-user'),
    path('logout/', views.logoutuser, name='logoutuser'),
    path('account/', views.account, name='account'),
    path('profile-user/', views.profile_user, name='profile-user'),
    path('edit-profile/', views.edit_profile, name='edit-profile'),
    path('body/', views.body, name='body'),
    path('update_body/', views.update_body, name='update_body'),
]


