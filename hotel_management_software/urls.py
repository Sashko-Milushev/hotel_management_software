
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel_management_software.common.urls')),
    path('accounts/', include('hotel_management_software.accounts.urls')),
    path('rooms/', include('hotel_management_software.rooms.urls')),
    path('reservations/', include('hotel_management_software.reservations.urls'))
]
