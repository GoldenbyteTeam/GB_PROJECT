from django.urls import path
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
    path('activate/<uidb64>/<token>/', ActivateView.as_view(), name="activate"),
    path('check-email/', CheckEmailView.as_view(), name="check_email"),
    path('success/', SuccessView.as_view(), name="success"),
]

handler404 = 'landingpage.views.error_404_view'