from django.shortcuts import render

from django.contrib.auth import views as auth_view, get_user_model
from django.urls import reverse_lazy

UserModel = get_user_model()


class SignInView(auth_view.LoginView):
    template_name = 'accounts/sign-in-page.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['logged_in_user'] = 'In' if self.request.user.is_authenticated else 'Not in'
        return context

    def get_success_url(self):
        if self.success_url:
            return self.success_url
        else:
            return self.get_redirect_url() or self.get_default_redirect_url()


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('login user')


class ChangePasswordView(auth_view.PasswordChangeView):
    template_name = 'accounts/change-password-page.html'


class ChangePasswordDoneView(auth_view.PasswordChangeDoneView):
    template_name = 'accounts/change-password-done-page.html'
