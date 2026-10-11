from django.urls import path
# from customUserAuth.views import view_customAuth  #//single function accrerss
from .views import *
from django.contrib.auth import views as auth_views



urlpatterns=[
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', RegisterView.as_view(), name='signup'),
    path('profile/', profile_view, name='profile'),
    # path('password_change/', auth_views.PasswordChangeView.as_view(template_name='customuserauth/password_changes.html'), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='customuserauth/password_change_done.html'), name='password_change_done'),
    path('password_change/', CustomPasswordChangeView.as_view(), name='password_change'),
]