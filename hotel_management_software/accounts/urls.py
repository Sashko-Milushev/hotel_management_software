from django.urls import path

from hotel_management_software.accounts.views import SignInView, ChangePasswordView, ChangePasswordDoneView, SignOutView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('change-password-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('user/<int:pk>/password-change/', ChangePasswordView.as_view(), name='change password')
)
