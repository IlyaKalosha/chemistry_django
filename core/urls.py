from django.urls import path, include
from .views import Home, Signup, Pills, Recipes, Orders

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('pills/', Pills.as_view(), name='pills'),
    path('recipes/', Recipes.as_view(), name='recipes'),
    path('sellers/', Recipes.as_view(), name='sellers'),
    path('orders/', Orders.as_view(), name='orders'),
    path('storage/', Recipes.as_view(), name='storage'),
    path('signup/', Signup.as_view(), name='signup'),
    path('accounts/', include('django.contrib.auth.urls'))
]
