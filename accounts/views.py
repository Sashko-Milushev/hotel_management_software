from django.shortcuts import render

from django.contrib.auth import views as auth_view, get_user_model
from django.urls import reverse_lazy

UserModel = get_user_model()


class SignInView(auth_view.LoginView):
    template_name = 'accounts/sign-in-page.html'


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('login user')


class ChangePasswordView(auth_view.PasswordChangeView):
    template_name = 'accounts/change-password-page.html'


class ChangePasswordDoneView(auth_view.PasswordChangeDoneView):
    template_name = 'accounts/change-password-done-page.html'
