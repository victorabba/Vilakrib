from django.urls import path, include
from.views import SignUpApiView, ContactApi
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('register/', SignUpApiView.as_view(), name='register'),
    path('contact/', ContactApi.as_view(), name='contact',),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]