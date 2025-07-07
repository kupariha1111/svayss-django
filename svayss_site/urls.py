from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # 🔗 Link to your app's urls
]
# This file defines the URL routing for the Django project.
# It includes the admin interface and routes requests to the main app's URLs.