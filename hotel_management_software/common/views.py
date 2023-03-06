from django.shortcuts import render
from django.views import generic as views


class HomeView(views.TemplateView):
    template_name = 'base/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['logged_in_user'] = 'In' if self.request.user.is_authenticated else 'Not in'
        context['is_superuser'] = 'Yes' if self.request.user.is_superuser else 'Not'
        return context
