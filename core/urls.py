from django.urls import path, include
from .views import Home, Signup, Pills


urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pills/', Pills.as_view(), name='pills'),
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))
]
