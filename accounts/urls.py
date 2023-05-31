from django.urls import path,re_path
from django.contrib.auth import views as auth_views


from . import views

from .views import (
    SignUpView,
    ActivateView,
    CheckEmailView,
    SuccessView,
)

print(auth_views.PasswordResetView)


urlpatterns = [
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('profile/', views.profile, name="users-profile"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('contributors/', views.contributors, name="contributors"),
    path(r'contributors/<int:user_id>', views.profile, name="users-profile"),
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('password/', views.CustomPasswordChangeView.as_view(), name="password"),
    path('password_success/',views.profile,name="password_change_done"),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name="password_reset"),
    path('success/', SuccessView.as_view(), name="success"),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    path('edit_profile/delete/<int:user_id>',views.delete_profile, name='delete_profile'),
]

handler404 = 'landingpage.views.error_404_view'
