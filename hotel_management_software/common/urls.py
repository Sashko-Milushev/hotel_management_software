from django.urls import path

from hotel_management_software.common.views import HomeView

urlpatterns = (
    path('', HomeView.as_view(), name='home'),
)