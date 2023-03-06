from django.urls import path

from accounts.views import SignInView, ChangePasswordView, ChangePasswordDoneView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('change-password-done/', ChangePasswordDoneView.as_view(), name='change password done'),
    path('user/<int:pk>/password-change/', ChangePasswordView.as_view(), name='change password')
)
