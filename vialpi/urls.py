from django.urls import path, include
from.views import SignUpApiView, ContactApi
from django.contrib.auth import views as auth_views



urlpatterns =[
    path('register/', SignUpApiView.as_view(), name='register'),
    path('contact/', ContactApi.as_view(), name='contact',),
]