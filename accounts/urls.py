from django.urls import path
from django.contrib.auth import views as auth_views


from . import views

from .views import (
    SignUpView,
    ActivateView,
    CheckEmailView,
    SuccessView,
)


urlpatterns = [
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', views.profile, name="users-profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='change-password.html'), name="password"),
    path('password_success/',views.profile,name="password_change_done"),
    path('success/', SuccessView.as_view(), name="success"),
]

handler404 = 'landingpage.views.error_404_view'