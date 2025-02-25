from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignInView


urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
