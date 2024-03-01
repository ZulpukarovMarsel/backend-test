from django.urls import path, include
from .views import SignUpAPIView, SignInAPIView, LogoutAPIView

urlpatterns = [
    # path('accounts/', include('allauth.urls')),
    path('sign_up/', SignUpAPIView.as_view()),
    path('sign_in/', SignInAPIView.as_view()),
    path('sign_out/', LogoutAPIView.as_view()),
]
