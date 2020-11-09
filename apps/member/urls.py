from django.urls import path

from apps.member.views import SignInView, SignUpView, UserDatailView, UserEmailConfirmView

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('signin/', SignInView.as_view()),
    path('user-detail/', UserDatailView.as_view()),
    path('user-confirm/<str:key>/', UserEmailConfirmView.as_view()),
]
