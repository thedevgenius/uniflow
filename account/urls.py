from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import SignInView, SignUpView, activate_account


urlpatterns = [
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('activate/<str:uidb64>/<str:token>/', activate_account, name='activate')
]
