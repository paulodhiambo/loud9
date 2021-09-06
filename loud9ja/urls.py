from django.urls import path

from loud9ja.views import RegisterView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
]
