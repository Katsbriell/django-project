from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('tasks.urls')),  # Include the URLs from the tasks app
]
