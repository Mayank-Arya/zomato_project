from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('menu/', include('menu.urls')),  # Include menu app's URLs
    # Define URLs for other apps as needed
]
