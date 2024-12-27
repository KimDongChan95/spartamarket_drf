from django.urls import path
from .views import UserRegisterAPIView
from .views import LoginAPIView
from .views import UserProfileAPIView

urlpatterns = [
    path('register/', UserRegisterAPIView.as_view(), name='user-register'),
    path('login/', LoginAPIView.as_view(), name='user-login'),
    path('profile/', UserProfileAPIView.as_view(), name='user-profile'),
]   