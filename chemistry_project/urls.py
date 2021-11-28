
from django.contrib import admin
from django.urls import path, include
from .views import HealthCheckView


urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('healthy/', HealthCheckView.as_view(), name="healthy")
]
